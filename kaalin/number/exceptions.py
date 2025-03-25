class NumberRangeError(Exception):
  def __init__(self, message="San shegaradan asıp ketti, maksimum decillion (1 000 000 000 000 000 000 000 000 000 000 000)"):
    self.message = message
    super().__init__(self.message)
