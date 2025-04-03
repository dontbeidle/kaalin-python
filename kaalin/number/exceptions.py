class NumberRangeError(Exception):
  def __init__(self, message="Number exceeded limit"):
    self.message = message
    super().__init__(self.message)
