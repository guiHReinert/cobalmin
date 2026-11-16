import os, shutil
import cobalmin.paths as paths
from cobalmin.model.stockpile import Stockpile
from time import sleep

class Miner():
  def __init__(self, stockpile):
    self.stockpile = stockpile
    
  
  def backup_markdown_files(self):
    BACKUP_DIR = paths.TEMP_DIR / "backup"
    if BACKUP_DIR not in paths.TEMP_DIR.iterdir():
      os.mkdir(BACKUP_DIR)
    
    for file in self.stockpile.markdown_files:
      shutil.copy(file, BACKUP_DIR)
      return BACKUP_DIR

  def clean_titles(self):
    for path in self.stockpile.markdown_files():
      with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        for line in text.split("\n"):
          print(line)
          sleep(0.5)
          