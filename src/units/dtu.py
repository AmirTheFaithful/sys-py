from unit import Port, Unit
from env.colors import RED, RESET
from env.exceptions import NoFreePorts

# Data Transport Unit
class DTU:
  _store: dict[str, Port]
  _dest: Unit | None

  def __init__(self):
    self._store = {}
    self._dest = None
  
  def connect(self, dest: Unit) -> int:
    try:
      free_port = dest.get_free_port()
    except NoFreePorts:
      print(RED + "No free ports found in unit " + RESET)