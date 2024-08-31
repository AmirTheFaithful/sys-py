from units.unit import Unit
from units.dtu import DTU

def main() -> None:
  my_unit = Unit()
  my_dtu = DTU()

  my_dtu.connect(my_unit)

if __name__ == "__main__":
  main()