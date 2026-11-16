import os
from cobalmin.model.ore import Ore

class Stockpile():
  def __init__(self, path):
    if os.path.isdir(path):
      self.path = path
    else:
      raise NotADirectoryError("\"{}\" is not a valid directory.".format(path))
    
    ores = []
    with os.scandir(self.path) as scan:
      for entry in scan:
        if entry.is_file() and entry.name.lower().endswith(".md"):
          ores.append(Ore(entry.path))
    self.ores = sorted(ores, key=lambda x: x.path)
    
  def __str__(self):
    return "{}".format(self.path)
