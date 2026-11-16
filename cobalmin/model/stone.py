from .ore import Ore

class Stone():
  def __init__(self, ore_out, ore_in, type):
    if isinstance(ore_out, Ore):
      self.ore_out = ore_out
    else:
      raise TypeError("\"{}\" is not a valid Ore object".format(ore_out))
    
    if isinstance(ore_in, Ore):
      self.ore_in = ore_in
    else:
      raise TypeError("\"{}\" is not a valid Ore object".format(ore_in))
    
    if isinstance(type, str):
      self.type = type
    else:
      raise TypeError("\"{}\" is not a valid String object".format(type))
    