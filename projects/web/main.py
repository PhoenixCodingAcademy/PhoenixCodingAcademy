'''
From the command line, run:
  flask --app main.py --debug run
This will start the Flask web but watch it for changes and automatically reload the site.
'''
import glob
import os
import re
import sys
import yaml
from urllib.parse import quote

thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))
sys.path.insert(0, root)
# print("root", root)
# print("sys.path", sys.path)


import libs.tools as tools
from libs.school import *
from libs.exam import *
from libs.search import Search

from flask import Flask, Blueprint, render_template, request, send_file, redirect, send_from_directory
from api import *

#fnStartup = tools.GetAncestorPath('startup.yaml')
#startup = tools.readYaml(fnStartup)


site = Blueprint('PCA', __name__, template_folder='templates')
app = Flask(__name__)

app.register_blueprint(get_name)

def RepoRoot():
  'Get the absolute folder path that contains the .git folder.'
  gp = tools.GetAncestorPath('.git')
  return os.path.abspath(os.path.join(gp, '..'))



def getModel(title):
  model = tools.Expando()
  model.school = getSchool()
  model.title = title
  model.request = request
  model.Markdown = Markdown
  return model




@app.route('/')
def hello():
  school = getSchool()
  model = getModel('PCA')
  model.FileMarkdown = FileMarkdown
  return render_template('main.html', model=model)


@app.route('/info')
def info():
  gp = tools.GetAncestorPath('.git')
  root = os.path.join(gp, '..')
  return f'''
<pre>
os.path.abspath('.'):         {os.path.abspath('.')}
app.instance_path:            {app.instance_path}
os.path.abspath(sys.argv[0]): {os.path.abspath(sys.argv[0])}
Repo Root:                    {os.path.abspath(root)}
.git:                         {os.path.abspath(gp)}
</pre>
'''


@app.route('/yaml')
def _yaml():
  model = getModel('YAML')
  return render_template('yaml.html', model=model)
  return f'''
<pre>
PATH: {os.path.abspath('.')}
</pre>
'''


@app.route('/subjects')
def _subjects():
  model = getModel('Subjects')
  model.school = getSchool()
  return render_template('subjects.html', model=model)


@app.route('/subjects/<id>')
def _subject(id):
  school = getSchool()
  subject = school[id]
  if not subject:
    model = getModel(id)
    model.message = f"Item '{id}' not found."
    return render_template('error.html', model=model)

  if not isinstance(subject, Subject):
    model = getModel('ERROR')
    model.message = f"Item '{id}' is not a Subject, but rather a '{type(subject)}'."
    return render_template('error.html', model=model)

  model = getModel(subject.title)
  model.subject = subject
  return render_template('subject.html', model=model)


@app.route('/courses/<id>')
def _course(id):
  school = getSchool()
  course = school[id]
  if not course:
    model = getModel(id)
    model.message = f"Item '{id}' not found."
    return render_template('error.html', model=model)

  if not isinstance(course, Course):
    model = getModel('ERROR')
    model.message = f"Item '{id}' is not a Course, but rather a '{type(course)}'.",
    return render_template('error.html', model=model)

  model = getModel(course.title)
  model.course = course
  return render_template('course.html', model=model)


@app.route('/exams')
def _exam():
  model = getModel('Exams')
  model.yamlFiles = [os.path.splitext(os.path.basename(x))[0] for x in glob.glob(os.path.join(tools.GetAncestorPath('data'), 'questions', '*.yaml')) if not os.path.basename(x).startswith('_')]
  model.yamlFiles.sort()
  model.questions = []
  model.seed = random.randint(1, 999999999)
  return render_template('exams.html', model=model)


@app.route('/startexam', methods=['POST'])
def _startexam():
  import random
  import hashlib
  
  data = request.json
  selectedYaml = data.get('selectedYaml', '')
  maxPoints = data.get('maxPoints', 50)
  maxDifficulty = data.get('maxDifficulty', 7)
  seed = data.get('seed', None)
  
  # Generate random seed if not provided
  if seed is None:
    seed = random.randint(1, 999999)
  else:
    seed = int(seed)
  
  # Set the random seed for reproducibility
  random.seed(seed)
  
  # Load the YAML file
  yamlPath = os.path.join(tools.GetAncestorPath('data'), 'questions', selectedYaml + '.yaml')
  if not os.path.exists(yamlPath):
    return jsonify({'error': 'YAML file not found'}), 404

  try:  
    yamlData = tools.readYaml(yamlPath)
  except Exception as e:
    print(e)
    error = {'error': f'Error reading YAML file "{selectedYaml}": {e.problem} at line {e.context_mark.line}'}
    return jsonify(error), 500
  
  # Filter questions by difficulty
  allQuestions = yamlData.get('questions', [])
  questions = [q for q in allQuestions if q.get('points', 1) <= maxDifficulty]
  
  # Shuffle questions (using the seeded random)
  random.shuffle(questions)
  
  # Select enough questions to reach maxPoints
  selected = []
  totalPts = 0
  for q in questions:
    if selected and totalPts >= maxPoints:
      break
    selected.append(q)
    totalPts += q.get('points', 1)
  
  # Build per-question randomized answers
  secret = 'exam_secret_key'
  for idx, q in enumerate(selected):
    allAnswers = []
    
    # Collect right answers
    rightAnswers = q.get('right', [])
    if not isinstance(rightAnswers, list):
      rightAnswers = [rightAnswers] if rightAnswers else []
    allAnswers.extend([{**a, 'isRight': True} for a in rightAnswers])
    
    # Collect wrong answers
    wrongAnswers = q.get('wrong', [])
    if not isinstance(wrongAnswers, list):
      wrongAnswers = [wrongAnswers] if wrongAnswers else []
    allAnswers.extend([{**a, 'isRight': False} for a in wrongAnswers])
    
    # Shuffle and pick 5
    random.shuffle(allAnswers)
    five = allAnswers[:5]
    
    # Check if any of the selected 5 answers are correct
    hasCorrectAnswer = any(a.get('isRight', False) for a in five)
    
    # Add "None of the above" - it's correct only if there are no correct answers in the list
    five.append({
      'answer': 'None of the above',
      'isRight': not hasCorrectAnswer,
      'isNoneOfTheAbove': True
    })
    
    # Generate UIDs
    for ansIdx, a in enumerate(five):
      hashStr = f"{secret}-{a.get('answer', '')}-{'RIGHT' if a.get('isRight', False) else 'WRONG'}"
      hashObj = hashlib.md5(hashStr.encode())
      a['uid'] = f"{idx}-{hashObj.hexdigest()[:8]}"
    
    q['displayAnswers'] = five
  
  return jsonify({
    'questions': selected,
    'totalPoints': totalPts,
    'history': yamlData.get('history', []),
    'seed': seed
  })


@app.route('/examreport')
def _examreport():
  model = getModel('Exam Report')
  
  # Load quizlog.yaml
  quizlogPath = os.path.join(tools.GetAncestorPath('reports'), 'quizlog.yaml')
  try:
    if os.path.exists(quizlogPath):
      model.quizlog = tools.readYaml(quizlogPath)
    else:
      model.quizlog = []
  except Exception as e:
    print(f"Error reading quizlog: {e}")
    model.quizlog = []
  
  return render_template('examreport.html', model=model)


@app.route('/gradeexam', methods=['POST'])
def _gradeexam():
  data = request.json
  name = data.get('name', '')
  quiz = data.get('quiz', '')
  maxPoints = data.get('maxPoints', 0)
  maxDifficulty = data.get('maxDifficulty', 0)
  history = data.get('history', [])
  answers = data.get('answers', [])
  questions = data.get('questions', [])
  score = 0
  for answer in answers:
    if answer.get('right', False):
      score += answer.get('points', 0)

  # Build questions array with full details
  questionLog = []
  print(f"DEBUG: Received {len(questions)} questions")
  for idx, q in enumerate(questions):
    print(f"DEBUG: Question {idx}: {q.get('question', 'NO QUESTION')}")
    print(f"DEBUG: DisplayAnswers: {len(q.get('displayAnswers', []))} answers")
    answerData = answers[idx] if idx < len(answers) else {}
    selectedUids = answerData.get('selected', [])
    
    # Build answer list with whether user correctly handled each answer
    answerList = []
    for ans in q.get('displayAnswers', []):
      answerIsCorrect = ans.get('isRight', False)
      userSelected = ans.get('uid', '') in selectedUids
      # User is correct if: (selected a correct answer) OR (didn't select a wrong answer)
      userHandledCorrectly = (userSelected and answerIsCorrect) or (not userSelected and not answerIsCorrect)
      
      answerList.append({
        'answer': ans.get('answer', ''),
        'isRight': answerIsCorrect,
        'selected': userSelected,
        'correct': userHandledCorrectly
      })
    
    questionLog.append({
      'question': q.get('question', ''),
      'points': q.get('points', 0),
      'right': answerData.get('right', False),
      'answers': answerList
    })
  print(f"DEBUG: Built {len(questionLog)} questions for log")

  # Create a YAML list object with one element:
  from datetime import datetime
  quizlog = {
    'student': name,
    'quiz': quiz,
    'maxDifficulty': maxDifficulty,
    'maxPoints': maxPoints,
    'history': history,
    'score': score,
    'takenOn': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'questions': questionLog
  }

  # Convert quizlog to a YAML string
  quizlogYaml = yaml.dump([quizlog])

  # Append quizlogYaml to the file "quizlog.yaml"
  quizlogPath = os.path.join(tools.GetAncestorPath('reports'), 'quizlog.yaml')
  with open(quizlogPath, 'a') as f:
    f.write(quizlogYaml)

  return jsonify({ 'results': { 'name': name, 'maxPoints': maxPoints, 'maxDifficulty': maxDifficulty, 'history': history, 'answers': answers, 'score': score }})


@app.route('/feedback')
def _feedback():
  #request.args
  model = getModel('Feedback')
  model.page = request.args.get("page", '')
  return render_template('feedback.html', model=model)


@app.route('/assignments/<id>')
def _assignment(id):
  school = getSchool()
  assignment = school[id]
  if not assignment:
    model = getModel('ERROR')
    model.message = f"Item '{id}' not found."
    return render_template('error.html', model=model)

  if not isinstance(assignment, Assignment):
    model = getModel('ERROR')
    model.message = f"Item '{id}' is not an Assignment, but rather a '{type(assignment)}'."
    return render_template('error.html', model=model)

  model = getModel(assignment.title)
  model.assignment = assignment
  return render_template('assignment.html', model=model)




@app.route('/pages')
def _pages():
  '''
  Get a list of all pages (*.md) under the "pages" folder.
  '''
  school = getSchool()

  # Get the absolute path to the "pages" folder.
  pagesPath = tools.GetAncestorPath('pages')
  title = "Pages"

  def recur(path):
    fps = glob.glob(os.path.join(path, "*"))
    fns = []
    for fp in fps:
      fp = fp.replace('/', os.path.sep)
      fp = fp.replace('\\', os.path.sep)
      fs = os.path.split(fp)
      fn = fs[1]
      if fn.startswith('/'): fn = fn[1:]
      if fn.startswith('_'): continue
      fns.append((os.path.join(fs[0], fn), fn))

    fns.sort(key=lambda x: str.lower(x[1]))

    html = '<ul>'
    for fp, fn in fns:
      fp = fp.replace('/', os.path.sep)
      fp = fp.replace('\\', os.path.sep)
      fn = fn.replace('/', os.path.sep)
      fn = fn.replace('\\', os.path.sep)

      if os.path.isdir(fp):
        h = recur(fp)
        name = fn
        html = html + f"""
<li class="expandable">{name}
<ul class="nested-ul">
    {h}
</ul>
</li>
        """
      else:
        # Build URL path relative to the pages root, URL-encoded for spaces etc.
        relpath = os.path.relpath(fp, pagesPath)
        relurl = "/pages/" + quote(relpath.replace(os.path.sep, '/'))
        name = os.path.splitext(fn)[0]
        print(f"fp: {fp}")
        try:
          text = tools.readFile(fp)
        except Exception as e:
          print(f"Error reading file: {fp}{e}")
          text = ""
        desc = ""
        match = re.search(r"DESCRIPTION:(?P<A>.*)", text)
        if match:
          desc = " - " + match.group("A").strip()
        html = html + f"""<li><a href="{relurl}">{name}</a><i>{desc}</i></li>"""
    html += '\n</ul>'
    return html

  html = recur(pagesPath)

  rootRepo = RepoRoot()
  webPath = os.path.join(rootRepo, 'projects', 'web')
  p = os.path.join(webPath, 'templates', "pages.html")
  p = "pages.html"
  model = getModel(title)
  model.html = html
  return render_template(p, model=model)





@app.route('/notebooks')
def _notebooks():
  school = getSchool()
  baseUrl = school.yo['data']['notebooks']['baseUrl']
  gitUrl = school.yo['data']['notebooks']['gitUrl']
  notebooksPath = tools.GetAncestorPath('projects/notebooks')
  meta = school.yo['data']['notebooks']['meta']

  cats = []
  for notebook in meta:
    cat = notebook['cat']
    if not cat in cats:
      cats.append(cat)

  html = ''

  for cat in cats:
    html += f'<h2>{cat}</h2>'
    html += '\n<ul>\n'
    for notebook in meta:
      thisCat = notebook['cat'] or 'Other'
      if thisCat != cat: continue
      fn = notebook['id']
      url = os.path.join(baseUrl, fn) + '.ipynb'
      giturl = os.path.join(gitUrl, fn) + '.ipynb'
      description = notebook['short']

      html += f"""<li><a href="{url}">{fn.replace('.ipynb', '')}</a> &nbsp; <a href="{giturl}">GIT</a>"""
      if description:
        html += f''' - <i>{description}</i>'''
      html += "</li>\n"
    html += '</ul>'

  model = getModel('Notebooks')
  model.path = notebooksPath
  model.html = html
  return render_template('notebooks.html', model=model)

@app.route('/notebooks/<id>')
def _notebook(id):
  '''
  @id (string) name like 'Sympy1.ipynb'
  '''
  school = getSchool()
  baseUrl = school.yo['data']['notebooks']['baseUrl']
  path = os.path.join(baseUrl, 'tree')
  return redirect(path, code=302)




@app.route('/client_example')
def _client_example():
  '''
  Example page that calls an API
  '''
  return render_template('client_example.html')




@app.route('/search')
def _search():
  '''

  '''
  term = request.args.get("search", '').lower()
  fn = tools.GetAncestorPath("projects/index.txt")
  db = tools.readText(fn)
  search = Search(db)

  school = getSchool()
  gitUrl = school.yo['data']['notebooks']['gitUrl']

  html = '<ul>'
  results = list(search.Search(term))
  if results:
    for sr in results:
      ws = ' '.join([f"<b>{w}</b> ({s*100:.2f})" for w,s in sorted(sr.wordScores.items(), key=lambda x: x[1])])
      if ws: ws = '- ' + ws
      text = sr.path
      if text.startswith(gitUrl):
        text = "JUPYTER: " + text[len(gitUrl):]
      html = html + f"""<li><a href="{sr.path}">{text}</a> {ws}</li>"""
    html += '\n</ul>'
  else:
    html = "No matches found"

  model = getModel(term)
  model.html = html
  return render_template("search.html", model=model)





@app.route('/<path:path>')
def _default(path):
  """
  The default catch-all path. If you hit https://DOMAIN/bananasplit, and there is no explicit route for "bananasplit",
  then this route will match, and path will be "bananasplit"
  """

  try:
    school = getSchool()
    rootRepo = RepoRoot()
    webPath = os.path.join(rootRepo, 'projects', 'web')
    title = path.split('/')[-1]

    if path.lower().endswith('.md'):
      path = os.path.join(rootRepo, path)
      data = tools.readDataFileWithUnicode(path)

      model = getModel(title)
      model.data = data
      return render_template('markdown.html', model=model)

    p = os.path.join(webPath, 'static', path)
    if os.path.exists(p):
      return send_file(p)

    p = os.path.join(webPath, 'templates', path)
    if os.path.exists(p):
      return render_template(path, model=getModel(title))

    p = os.path.join(webPath, 'templates', path + ".html")
    if os.path.exists(p):
      return render_template(path + ".html", model=getModel(title))

    dp = os.path.join(rootRepo, 'data')
    path = os.path.join(rootRepo, path)

    return render_template(f'{path}.html', model=getModel(title))
  except Exception as e:
    model = getModel(f'''{type(e).__name__}''')
    model.message = f'''{type(e).__name__}: {e}'''
    return render_template("error.html", model=model)



@app.route('/zips/<filename>', methods=['GET'])
def download(filename):
    downloads = os.path.join(app.root_path, 'zips')
    return send_from_directory(downloads, filename)



def precheck():
  """
  Load all YAML files in the "questions" folder to catch any YAML parse errors early before starting.
  """
  questionsPath = os.path.join(tools.GetAncestorPath('data'), 'questions')
  yamlFiles = glob.glob(os.path.join(questionsPath, '*.yaml'))

  ok = True
  for yamlFile in yamlFiles:
    if os.path.basename(yamlFile).startswith('_'):
      continue
    
    try:
      tools.readYaml(yamlFile)
      print(f"✓ Loaded: {os.path.basename(yamlFile)}")
    except Exception as e:
      print(f"✗ Error loading {os.path.basename(yamlFile)}: {e}")
      import re
      match = re.search(r'position (\d+)', str(e))
      if match:
        print(f"Position: {match.group(1)}")
        text = tools.readDataFileWithUnicode(yamlFile)
        print(f"{text[max(0, int(match.group(1))-20):int(match.group(1))+20]}")
      ok = False

  if not ok:
    print("✗ Some YAML files could not be loaded. Please fix the errors and try again.")
  return ok




if __name__ == "__main__":
  if precheck():
    app.run(host="0.0.0.0")
