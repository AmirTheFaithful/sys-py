from typing_extensions import Self, Union
from dataclasses import dataclass

@dataclass
class Port:
  id: str
  in_use: bool = False
  connected_to: Union[Self, None] = None
