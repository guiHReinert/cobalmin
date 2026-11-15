import os
from cobalmin import Reader

base = os.path.dirname(os.path.abspath(__file__))

original_path = "~/home/guilherme-hoerning-reinert/cobalto/markdown"

# path_markdown = os.path.join(base, original_path)
path_markdown = original_path


zetter = Reader(path_markdown)
zetter.clean_titles()

