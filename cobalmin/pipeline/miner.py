import os, shutil
import cobalmin.paths as paths
from cobalmin.model.stockpile import Stockpile

class Miner():
  def __init__(self, stockpile):
    if isinstance(stockpile, Stockpile):
      self.stockpile = stockpile
    else:
      raise TypeError("\"{}\" is not a valid Stockpile object".format(stockpile))
  
  def backup_ores(self):
    BACKUP_DIR = paths.TEMP_DIR / "backup"
    if BACKUP_DIR not in paths.TEMP_DIR.iterdir():
      os.mkdir(BACKUP_DIR)
    
    for ore in self.stockpile.ores:
      shutil.copy(ore, BACKUP_DIR)
      return BACKUP_DIR

# TESTE
  def print_ores_text(self):
    for ore in self.stockpile.ores:
      print(ore.text)
          