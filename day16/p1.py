import sys
from collections import defaultdict
from heapq import heappush, heappop

# 0: East, 1: South, 2: West, 3: North
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main() -> None:
  maze = open(sys.argv[1]).read().splitlines()
  sr, sc = len(maze) - 2, 1

  pq = [(0, sr, sc, 0)]
  seen = defaultdict(lambda: float("inf"))
  seen[(sr, sc, 0)] = 0
  min_cost = float("inf")

  while pq:
    cost, cr, cc, cdir = heappop(pq)

    if maze[cr][cc] == "E":
      min_cost = min(min_cost, cost)
      continue

    # -1: turn left, 0: go straight, 1: turn right
    for turn in [-1, 0, 1]:
      ndir = (cdir + turn) % 4
      new_cost = cost + (1000 if turn != 0 else 0)
      nr, nc = cr + DIRS[ndir][0], cc + DIRS[ndir][1]

      if maze[nr][nc] != "#":
        new_cost += 1

        if new_cost < seen[(nr, nc, ndir)]:
          seen[(nr, nc, ndir)] = new_cost
          heappush(pq, (new_cost, nr, nc, ndir))

  print(min_cost)


if __name__ == "__main__":
  main()