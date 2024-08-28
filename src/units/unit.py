from dataclasses import dataclass
from uuid import uuid4
from typing import Any

# Local imports
from env.colors import GREEN, BLUE, RESET

@dataclass
class Port:
  id: str
  in_use: bool

# Data Transport Unit
class DTU:
  _store: dict[str, Port]

  def __init__(self):
    self._store = {}

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
      port: Port = Port(id=port_id, in_use=False)
      self._ports[port_id] = port
  
  # Log short info about each port
  def log_ports(self) -> None:
    for id, port in self._ports.items():
      print(GREEN + f"{id}" + RESET + ": " + BLUE + f"{port.in_use}" + RESET)