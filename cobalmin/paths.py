# This file defines the most crucial relative paths
import os
from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_DIR.parent
RESOURCES_DIR = PACKAGE_DIR/"resources"

TEMP_DIR = PACKAGE_DIR/"temp"
if TEMP_DIR not in PACKAGE_DIR.iterdir():
  os.mkdir(TEMP_DIR)

def resource_path(*parts):
  path = RESOURCES_DIR.joinpath(*parts)
  if not path.exists():
    raise FileNotFoundError("Resource not found: {}".format(path))
  return path
  
