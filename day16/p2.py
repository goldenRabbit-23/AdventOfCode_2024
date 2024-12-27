import sys
from collections import defaultdict
from heapq import heappush, heappop

# 0: East, 1: South, 2: West, 3: North
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main() -> None:
  maze = open(sys.argv[1]).read().splitlines()
  sr, sc = len(maze) - 2, 1
  er, ec = 1, len(maze[0]) - 2

  # Part 1: Forward search from start
  pq = [(0, sr, sc, 0)]
  costs_from_start = defaultdict(lambda: float("inf"))
  costs_from_start[(sr, sc, 0)] = 0
  min_cost = float("inf")

  while pq:
    cost, cr, cc, cdir = heappop(pq)

    if (cr, cc) == (er, ec):
      min_cost = min(min_cost, cost)
      continue

    # -1: turn left, 0: go straight, 1: turn right
    for turn in [-1, 0, 1]:
      ndir = (cdir + turn) % 4
      new_cost = cost + (1000 if turn != 0 else 0)

      if new_cost < costs_from_start[(cr, cc, ndir)]:
        costs_from_start[(cr, cc, ndir)] = new_cost
        heappush(pq, (new_cost, cr, cc, ndir))

      nr, nc = cr + DIRS[ndir][0], cc + DIRS[ndir][1]

      if maze[nr][nc] != "#":
        new_cost += 1

        if new_cost < costs_from_start[(nr, nc, ndir)]:
          costs_from_start[(nr, nc, ndir)] = new_cost
          heappush(pq, (new_cost, nr, nc, ndir))

  # Part 2: Backward search from end
  pq = [(0, er, ec, 1), (0, er, ec, 2)]
  costs_from_end = defaultdict(lambda: float("inf"))
  costs_from_end[(er, ec, 1)] = 0
  costs_from_end[(er, ec, 2)] = 0

  while pq:
    cost, cr, cc, cdir = heappop(pq)

    if (cr, cc) == (sr, sc):
      continue

    for turn in [-1, 0, 1]:
      ndir = (cdir + turn) % 4
      new_cost = cost + (1000 if turn != 0 else 0)

      if new_cost < costs_from_end[(cr, cc, ndir)]:
        costs_from_end[(cr, cc, ndir)] = new_cost
        heappush(pq, (new_cost, cr, cc, ndir))

      nr, nc = cr + DIRS[ndir][0], cc + DIRS[ndir][1]

      if maze[nr][nc] != "#":
        new_cost += 1

        if new_cost < costs_from_end[(nr, nc, ndir)]:
          costs_from_end[(nr, nc, ndir)] = new_cost
          heappush(pq, (new_cost, nr, nc, ndir))

  optimal_tiles = set()

  for (r, c, d), cost_from_start in costs_from_start.items():
    if cost_from_start + costs_from_end[(r, c, (d + 2) % 4)] == min_cost:
      optimal_tiles.add((r, c))

  print(len(optimal_tiles))


if __name__ == "__main__":
  main()