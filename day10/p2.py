import sys
from collections import deque


def main() -> None:
  topo_map = open(sys.argv[1]).read().splitlines()
  topo_map = [[int(height) for height in row] for row in topo_map]
  rows, cols = len(topo_map), len(topo_map[0])
  trailheads = []

  # find all trailheads
  for r, row in enumerate(topo_map):
    for c, height in enumerate(row):
      if height == 0:
        trailheads.append((r, c))

  q = deque()
  rating = 0

  for sr, sc in trailheads:
    sub_rating = 0
    q.append((sr, sc))

    while q:
      cr, cc = q.popleft()

      if topo_map[cr][cc] == 9:
        sub_rating += 1

      for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr = cr + dr
        nc = cc + dc

        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
          continue

        # gradual uphill
        if topo_map[nr][nc] == topo_map[cr][cc] + 1:
          q.append((nr, nc))

    rating += sub_rating

  print(rating)


if __name__ == "__main__":
  main()