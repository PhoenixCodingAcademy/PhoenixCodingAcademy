import jaro
import os
import re
import sys
import glob

thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))
sys.path.insert(0, root)

import yaml
from io import StringIO
import libs.tools as tools




class SearchResult:
  def __init__(self, path, wordScores):
    self.path = path
    self.wordScores = wordScores





class Search:
  def __init__(self, db):
    """_summary_

    Args:
        db (string): a text file where each line in in the format:
          WORD: PATH,...
        example:
          apl: /subjects/programming,/subjects/computers,/subjects/computers,/subjects/computers
    """

    if not db: raise Exception("@db is null")
    self.db = {}

    for line in db.splitlines():
      word = line.split(':')[0]
      paths = line.split(':')[1].strip().split(',')
      self.db[word] = paths

  def Search(self, text):
    paths = {}
    matches = re.finditer(r"[a-z]+", text)
    mm = {}
    for match in matches:
      word = match.group(0)
      for w in self.db:
        if w == word:
          score = 30
        else:
          score = jaro.jaro_winkler_metric(word, w)
        if score > .8:
          for path in self.db[w]:
            d = paths.get(path, {})
            d[w] = score
            paths[path] = d
    for path, ws in sorted(paths.items(), key=lambda x: -sum(score for w, score in x[1].items())):
      yield SearchResult(path, ws)





  def Search1(self, text):
    paths = {}
    matches = re.finditer(r"[a-z]+", text)
    for match in matches:
      word = match.group(0)
      if word in self.db:
        for path in self.db[word]:
          count = paths.get(path, 0)
          paths[path] = count + 1
    for path, score in sorted(paths.items(), key=lambda x: -x[1]):
      yield SearchResult(path, score)







if __name__ == "__main__":
  fn = tools.GetAncestorPath("projects/index.txt")
  db = tools.readFile(fn)
  search = Search(db)
  print("Num words =", len(search.db))

  for sr in search.Search("apl courses"):
    print(sr.score, sr.path)

  print("DONE")