import os
import json
import pypandoc
from time import sleep

class Zetter:
  def __init__(self, path):
    if os.path.isdir(path):
      self.path = path
    else:
      raise NotADirectoryError("\"{}\" is not a valid directory.".format(path))
    
  def markdown_files(self):
    path_markdown_files = []
    with os.scandir(self.path) as scan:
      for entry in scan:
        if entry.is_file() and entry.name.lower().endswith(".md"):
          path_markdown_files.append(entry.path)
    return sorted(path_markdown_files)
  
  def clean_titles(self):
    for path in self.markdown_files():
      with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
        
    
  def num_markdown(self):
    return len(self.markdown_files())
    
  def __str__(self):
    return "{}".format(self.path)

