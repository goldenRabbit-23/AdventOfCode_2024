import sys
from itertools import product


def main() -> None:
  schematics = open(sys.argv[1]).read().split("\n\n")
  locks = []
  keys = []

  for schematic in schematics:
    schematic = schematic.splitlines()
    schematic_T = ["".join(line) for line in zip(*schematic[1:6])]
    cnt = [sum(ch == "#" for ch in row) for row in schematic_T]
    (locks if schematic[0] == "#####" else keys).append(tuple(cnt))

  print(sum(all(x + y <= 5 for x, y in zip(lock, key))
            for lock, key in product(locks, keys)))


if __name__ == "__main__":
  main()