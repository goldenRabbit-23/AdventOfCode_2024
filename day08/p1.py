import sys
from collections import defaultdict
from itertools import combinations


def main() -> None:
  grid = open(sys.argv[1]).read().splitlines()
  rows, cols = len(grid), len(grid[0])
  antennas = defaultdict(list)

  for r, row in enumerate(grid):
    for c, freq in enumerate(row):
      if freq != ".":
        antennas[freq].append((r, c))

  antinodes = set()

  for locs in antennas.values():
    for (r1, c1), (r2, c2) in combinations(locs, 2):
      p1, q1 = 2 * r1 - r2, 2 * c1 - c2
      p2, q2 = 2 * r2 - r1, 2 * c2 - c1

      if 0 <= p1 < rows and 0 <= q1 < cols:
        antinodes.add((p1, q1))

      if 0 <= p2 < rows and 0 <= q2 < cols:
        antinodes.add((p2, q2))

  print(len(antinodes))


if __name__ == "__main__":
  main()