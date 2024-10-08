from uuid import uuid4
from typing import Any

from ds.linked_list import LinkedList

# Local imports
from env.colors import GREEN, BLUE, RESET
from env.exceptions import NoFreePorts, StorageDuplicateData

from units.port import Port

class Unit:
  _ports: dict[str, Port] = {}
  # For now, the storage will be just a dict
  _storage: LinkedList
  status: str

  def __init__(self):
    # First generate ports:
    self._gen_ports()

    self.storage = LinkedList()
    self.status = "public"

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
      if not port.in_use:
        return port
      else:
        continue
    
    raise NoFreePorts(msg="Unit has no free ports to connect.", err_code=500)
  
  def set_data(self, key: str, value: Any) -> None:
    # First check if such key exists
    if key in self._storage:
      raise StorageDuplicateData(msg=f"The storage of the unit already has the key \"{key}\"", err_code=501)
    else:
      self._storage[key] = value
