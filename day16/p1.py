import sys
from collections import defaultdict, deque


def main() -> None:
  maze = open(sys.argv[1]).read().splitlines()
  sr, sc = len(maze) - 2, 1
  dist = defaultdict(int)
  min_score = float("inf")

  q = deque([(sr, sc, 0, 1, 0)])
  dist[(sr, sc)] = 0

  while q:
    cr, cc, cdr, cdc, cs = q.popleft()

    # arrived at the end
    if maze[cr][cc] == "E":
      min_score = cs

    # move forward
    if maze[cr + cdr][cc + cdc] in ".E":
      if (cr + cdr, cc + cdc) not in dist or cs + 1 < dist[(cr + cdr, cc + cdc)]:
        q.append((cr + cdr, cc + cdc, cdr, cdc, cs + 1))
        dist[(cr + cdr, cc + cdc)] = cs + 1

    # move counter-clockwise
    if maze[cr - cdc][cc + cdr] in ".E":
      if (cr - cdc, cc + cdr) not in dist or cs + 1001 < dist[(cr - cdc, cc + cdr)]:
        q.append((cr - cdc, cc + cdr, -cdc, cdr, cs + 1001))
        dist[(cr - cdc, cc + cdr)] = cs + 1001

    # move clockwise
    if maze[cr + cdc][cc - cdr] in ".E":
      if (cr + cdc, cc - cdr) not in dist or cs + 1001 < dist[(cr + cdc, cc - cdr)]:
        q.append((cr + cdc, cc - cdr, cdc, -cdr, cs + 1001))
        dist[(cr + cdc, cc - cdr)] = cs + 1001

  print(min_score)


if __name__ == "__main__":
  main()