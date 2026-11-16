import os

class Ore():
  def __init__(self, path):
    if isinstance(path, str):
      self.path = path
    else:
      raise NotADirectoryError("\"{}\" is not a valid directory.".format(path))
    
    with open(path, "r", encoding="utf-8") as f:
      self.text = f.read()