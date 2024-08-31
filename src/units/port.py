from dataclasses import dataclass

@dataclass
class Port:
  id: str
  in_use: bool = False
  connected_to = None