from uuid import uuid4
from typing import Any

# Local imports
from env.colors import GREEN, BLUE, RESET
from env.exceptions import NoFreePorts

from port import Port

class Unit:
  _ports: dict[str, Port] = {}
  # For now, the storage will be just a dict
  _storage: dict[str, Any] = {}
  status: str = "public"

  def __init__(self):
    # First generate ports:
    self._gen_ports()

  def _gen_ports(self) -> None:
    if self._ports:
      return
    
    # Initialize three ports one by one
    for index in range(1, 4):
      port_id: str = f"U#{index}:{uuid4()}"
      port: Port = Port(id=port_id)
      self._ports[port_id] = port
  
  # Log short info about each port
  def log_ports(self) -> None:
    for id, port in self._ports.items():
      print(GREEN + f"{id}" + RESET + ": " + BLUE + f"{port.in_use}" + RESET)
  
  # Return first found free port, if it's so
  def get_free_port(self) -> Port:
    for port in self._ports.values():
      if port.in_use:
        return port
      else:
        continue
    
    raise NoFreePorts(msg="Unit has no free ports to connect.", err_code=500)
