import os
from cobalmin.paths import *
from cobalmin import Reader

original_dir = "/home/guilherme-hoerning-reinert/cobalto/markdown"

reader = Reader(original_dir)
reader.clean_titles()
