import sys
from collections import defaultdict
from itertools import combinations


def main() -> None:
  grid = open(sys.argv[1]).read().splitlines()
  rows, cols = len(grid), len(grid[0])
  antennas = defaultdict(list)
  antennas_set = set()

  for r, row in enumerate(grid):
    for c, freq in enumerate(row):
      if freq != ".":
        antennas[freq].append((r, c))
        antennas_set.add((r, c))

  antinodes = set()

  for locs in antennas.values():
    for (r1, c1), (r2, c2) in combinations(locs, 2):
      # (r1, c1) -> (r2, c2)
      dr, dc = r2 - r1, c2 - c1
      cr, cc = r2 + dr, c2 + dc

      while 0 <= cr < rows and 0 <= cc < cols:
        antinodes.add((cr, cc))
        cr += dr
        cc += dc

      # (r1, c1) <- (r2, c2)
      dr, dc = r1 - r2, c1 - c2
      cr, cc = r1 + dr, c1 + dc

      while 0 <= cr < rows and 0 <= cc < cols:
        antinodes.add((cr, cc))
        cr += dr
        cc += dc

  print(len(antinodes | antennas_set))


if __name__ == "__main__":
  main()