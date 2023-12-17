"""
Index all the pages
"""
import glob
import os
import re
import libs.tools
import libs.school

words = {}
def index(path, sentence):
  if not sentence: return
  sentence = sentence.lower()
  matches = re.finditer(r"[a-z]+", sentence)
  for match in matches:
    word = match.group(0)
    if len(word) < 2: continue
    if not word in words:
      words[word] = []
    list = words[word]
    list.append(path)
    words[word] = list


school = libs.school.getSchool()
data = libs.tools.GetAncestorPath("pages")
for fp in glob.glob(os.path.join(data, '*.md')):
  fn = os.path.split(fp)[1]
  text = libs.tools.readFile(fp)
  index(f"/pages/{fn}", text)

for subject in school.subjects:
  path = f"/subjects/{subject.id}"
  index(path, subject.title)
  index(path, subject.description)
  index(path, subject.short)
  index(path, subject.purpose)

  for course in subject.courses:
    path = f"/courses/{course.id}"
    index(path, course.title)
    index(path, course.description)
    index(path, course.short)
    index(path, course.purpose)

    for assignment in course.assignments:
      path = f"/assignments/{assignment.id}"
      index(path, assignment.title)
      index(path, assignment.description)
      index(path, assignment.short)
      index(path, assignment.purpose)

with open('index.txt', 'w') as f:
  for word, list in sorted(words.items()):
    f.write(f"{word}: {','.join(list)}\n")