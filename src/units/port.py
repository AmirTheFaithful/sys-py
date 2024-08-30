from dataclasses import dataclass

from port import Port

@dataclass
class Port:
  id: str
  in_use: bool = False
  connected_to: Port | None