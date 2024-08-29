from dataclasses import dataclass

@dataclass
class Port:
  id: str
  in_use: bool