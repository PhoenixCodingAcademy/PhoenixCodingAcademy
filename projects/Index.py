"""
Index all the pages
"""
import glob
import os
import re
import libs.tools
import libs.school



print("Indexing files...")

fileTypes = {}
words = {}

def index(path, sentence):
  '''
  Tokenize @sentence and associated each token with path.
  '''
  if not sentence: return
  sentence = sentence.lower()

  def doMatches(matches):
    for match in matches:
      word = match.group(0)
      if len(word) < 2: continue
      if not word in words:
        words[word] = []
      list = words[word]
      list.append(path)
      words[word] = list

  matches = re.finditer(r"[a-z]+", sentence)
  doMatches(matches)

  matches = re.finditer(r"[0-9]+", sentence)
  doMatches(matches)




school = libs.school.getSchool()

# INDEX ALL PAGES
data = libs.tools.GetAncestorPath("pages")
fileTypes['pages'] = 0
for fp in glob.glob(os.path.join(data, '**/*.md'), recursive=True):
  if 'ai' in fp:
    pass
  fn = fp[len(data) + 1:]
  text = libs.tools.readDataFile(fp)
  fn = fn.replace('\\', '/') # Url
  index(f"/pages/{fn}", text)
  fileTypes['pages'] = fileTypes['pages'] + 1


# INDEX ALL NOTEBOOKS
notebooks = school.yo['data']['notebooks']
gitUrl = notebooks['gitUrl']
for notebook in notebooks['meta']:
  id = notebook['id']
  short = notebook['short']
  cat = notebook['cat']
  if 'Gradient' in id:
    print()
  text = f"{id} {short} {cat}"
  index(f"{gitUrl}/{id}.ipynb", text)

# INDEX ALL SUBJECTS, COURSES, and ASSIGNMENTS
fileTypes['subjects'] = 0
fileTypes['courses'] = 0
fileTypes['assignments'] = 0

for subject in school.subjects:
  path = f"/subjects/{subject.id}"
  index(path, subject.id)
  index(path, subject.title)
  index(path, subject.description)
  index(path, subject.keywords)
  index(path, subject.short)
  index(path, subject.purpose)
  fileTypes['subjects'] = fileTypes['subjects'] + 1

  for course in subject.courses:
    path = f"/courses/{course.id}"
    index(path, course.id)
    index(path, course.title)
    index(path, course.description)
    index(path, course.keywords)
    index(path, course.short)
    index(path, course.purpose)
    fileTypes['courses'] = fileTypes['courses'] + 1

    for assignment in course.assignments:
      path = f"/assignments/{assignment.id}"
      index(path, assignment.id)
      index(path, assignment.title)
      index(path, assignment.description)
      index(path, assignment.keywords)
      index(path, assignment.short)
      index(path, assignment.purpose)
      fileTypes['assignments'] = fileTypes['assignments'] + 1

with open('index.txt', 'w') as f:
  for word, list in sorted(words.items()):
    f.write(f"{word}: {','.join(list)}\n")

n = sum([x[1] for x in fileTypes.items()])
print(f"Indexed {n} files:")
for k,v in fileTypes.items():
  print(f"  {k:<20}  {v}")