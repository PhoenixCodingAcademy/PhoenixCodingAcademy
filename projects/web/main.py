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
  #request.args
  model = getModel('Exams')
  return render_template('exams.html', model=model)


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
<li class="expandable">{name}<i>{desc}</i>
<ul class="nested-ul">
    {h}
</ul>
</li>
        """
      else:
        path = f"/pages/{fn}"
        name = fn[:-3]
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
        html = html + f"""<li><a href="{path}">{name}</a><i>{desc}</i></li>"""
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
  db = tools.readDataFile(fn)
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
      data = tools.readDataFile(path)
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



if __name__ == "__main__":
  app.run(host="0.0.0.0")
