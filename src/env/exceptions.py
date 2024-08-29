class NoFreePorts(Exception):
  message: str

  def __init__(self, message: str, err_code: int):
    self.message = message
    self.err_code = err_code
    super().__init__(self.message)

  def __str__(self):
    return f"{self.message} (Error code: {self.err_code})"