#!/venv/bin/python
import os
from classes import Zetter

def walk_printer (lst):
  for item in lst:
    print(item)
    if isinstance(item, list):
      walk_printer(item)

base = os.path.dirname(os.path.abspath(__file__))
path_markdown = os.path.join(base, "markdown")

zetter = Zetter(path_markdown)
zetter.clean_titles()

