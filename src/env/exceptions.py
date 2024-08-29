class NoFreePorts(Exception):
  message: str

  def __init__(self, msg: str, err_code: int):
    self.message = msg
    self.err_code = err_code
    super().__init__(self.message)

  def __str__(self):
    return f"{self.message} (Error code: {self.err_code})"