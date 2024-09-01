from enum import Enum

class ErrorCodes(Enum):
  NO_FREE_PORTS = 500
  STRG_DPLCT_DT = 501

class ExceptionHandler:
  _exception: Exception
  def __init__(self, exception: Exception):
    self._exception = exception
  
  def log_exc(self) -> None:
    print(str(self._exception))

class NoFreePorts(Exception):
  message: str

  def __init__(self, msg: str):
    self.message = msg
    self.err_code = ErrorCodes.NO_FREE_PORTS
    self.name = str(ErrorCodes(self.err_code))
    super().__init__(self.message)

  def __str__(self):
    return f"\nName: {self.name}\n Message: {self.message}\n Error code: {self.err_code})\n"

class StorageDuplicateData(Exception):
  massage: str

  def __init__(self, msg: str):
    self.message = msg
    self.err_code = ErrorCodes.STRG_DPLCT_DT
    self.name = str(ErrorCodes(self.err_code))
    super().__init__(self.message)