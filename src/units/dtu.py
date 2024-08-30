from uuid import uuid

# Local imports
from unit import Port, Unit
from env.colors import RED, RESET
from env.exceptions import NoFreePorts
from port import Port

# Data Transport Unit
class DTU:
  _store: dict[str, Port]
  _dest: Unit | None
  _port: Port

  def __init__(self):
    self._store = {}
    self._dest = None
    self._port = Port(uuid())
  
  def connect(self, dest: Unit) -> int:
    try:
      free_port = dest.get_free_port()
    except NoFreePorts:
      print(RED + "No free ports found in unit " + RESET)
    
    free_port.in_use = True
    self._port.in_use = True
    free_port.connected_to = self._port
    self._port.connected_to = free_port