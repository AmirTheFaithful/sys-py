from uuid import uuid4
from typing import Optional

# Local imports
from units.port import Port
from units.unit import Unit
from env.colors import RED, RESET
from env.exceptions import NoFreePorts
from enum import Enum

class DTUFlags(Enum):
  TRANSFER = 0

# Data Transport Unit
class DTU:
  _store: dict[str, Port]
  _dest: Optional[Unit]
  _port: Port
  _flag: int

  def __init__(self, flag: int):
    self._store = {}
    self._dest = None
    self._port = Port(uuid4())
    self._flag = flag
  
  def connect(self, dest: Unit) -> int:
    try:
      free_port = dest.get_free_port()
    except NoFreePorts:
      print(RED + "No free ports found in unit " + RESET)
    else:
      free_port.in_use = True
      self._port.in_use = True
      free_port.connected_to = self._port
      self._port.connected_to = free_port