class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return self.args