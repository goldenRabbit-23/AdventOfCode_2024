import sys
from collections import defaultdict
from heapq import heappush, heappop

# 0: East, 1: South, 2: West, 3: North
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dijkstra(maze, sr, sc, sdir, er, ec, costs) -> int:
  pq = []
  min_cost = float("inf")

  for d in sdir:
    pq.append((0, sr, sc, d))
    costs[(sr, sc, d)] = 0

  while pq:
    cost, cr, cc, cdir = heappop(pq)

    if (cr, cc) == (er, ec):
      min_cost = min(min_cost, cost)
      continue

    # -1: turn left, 0: go straight, 1: turn right
    for turn in [-1, 0, 1]:
      ndir = (cdir + turn) % 4
      new_cost = cost + (1000 if turn != 0 else 0)

      if new_cost < costs[(cr, cc, ndir)]:
        costs[(cr, cc, ndir)] = new_cost
        heappush(pq, (new_cost, cr, cc, ndir))

      nr, nc = cr + DIRS[ndir][0], cc + DIRS[ndir][1]

      if maze[nr][nc] != "#":
        new_cost += 1

        if new_cost < costs[(nr, nc, ndir)]:
          costs[(nr, nc, ndir)] = new_cost
          heappush(pq, (new_cost, nr, nc, ndir))

  return min_cost


def main() -> None:
  maze = open(sys.argv[1]).read().splitlines()
  sr, sc = len(maze) - 2, 1
  er, ec = 1, len(maze[0]) - 2
  costs_from_start = defaultdict(lambda: float("inf"))
  costs_from_end = defaultdict(lambda: float("inf"))

  # Part 1: Forward search from start
  min_cost = dijkstra(maze, sr, sc, (0,), er, ec, costs_from_start)

  # Part 2: Backward search from end
  dijkstra(maze, er, ec, (1, 2), sr, sc, costs_from_end)

  # Part 3: Count tiles which are on an optimal path
  optimal_tiles = set()

  for (r, c, d), cost_from_start in costs_from_start.items():
    if cost_from_start + costs_from_end[(r, c, (d + 2) % 4)] == min_cost:
      optimal_tiles.add((r, c))

  print(len(optimal_tiles))


if __name__ == "__main__":
  main()