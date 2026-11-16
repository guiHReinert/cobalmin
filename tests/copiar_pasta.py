from cobalmin.model.stockpile import Stockpile
from cobalmin.pipeline.miner import Miner

original_dir = "/home/guilherme-hoerning-reinert/cobalto/markdown"

stockpile = Stockpile(original_dir)
miner = Miner(stockpile)
miner.clean_titles()
