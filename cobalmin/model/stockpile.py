import os

class Stockpile():
  def __init__(self, path):
    if os.path.isdir(path):
      self.path = path
    else:
      raise NotADirectoryError("\"{}\" is not a valid directory.".format(path))
    
  def markdown_files(self):
    markdown_files = []
    with os.scandir(self.path) as scan:
      for entry in scan:
        if entry.is_file() and entry.name.lower().endswith(".md"):
          markdown_files.append(entry.path)
    return sorted(markdown_files)
    
  def num_markdown(self):
    return len(self.markdown_files())
    
  def __str__(self):
    return "{}".format(self.path)

