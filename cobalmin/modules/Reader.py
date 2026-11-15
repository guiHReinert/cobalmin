import os, shutil, json
import pypandoc
from cobalmin.paths import *
from time import sleep

class Reader:
  def __init__(self, path):
    if os.path.isdir(path):
      self.path = path
    else:
      raise NotADirectoryError("\"{}\" is not a valid directory.".format(path))
    
  def backup_markdown_files(self):
    markdown_files = []
    with os.scandir(self.path) as scan:
      for entry in scan:
        if entry.is_file() and entry.name.lower().endswith(".md"):
          markdown_files.append(entry.path)
          
    BACKUP_DIR = TEMP_DIR/"backup"
    if BACKUP_DIR not in TEMP_DIR.iterdir():
      os.mkdir(BACKUP_DIR)
    
    for file in markdown_files:
      shutil.copy(file, BACKUP_DIR)
    return BACKUP_DIR
    
  def markdown_files(self):
    markdown_files = []
    with os.scandir(self.backup_markdown_files()) as scan:
      for entry in scan:
        if entry.is_file() and entry.name.lower().endswith(".md"):
          markdown_files.append(entry.path)
    return sorted(markdown_files)
    
  def clean_titles(self):
    for path in self.markdown_files():
      with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        for line in text.split("\n"):
          print(line)
          sleep(0.5)
        
    
  def num_markdown(self):
    return len(self.markdown_files())
    
  def __str__(self):
    return "{}".format(self.path)

