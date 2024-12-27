import sys
from collections import deque


def main() -> None:
  track = list(map(list, open(sys.argv[1]).read().splitlines()))
  rows, cols = len(track), len(track[0])

  for r, row in enumerate(track):
    for c, ch in enumerate(row):
      if ch == "S":
        sr, sc = r, c


  def simulate() -> int:
    q = deque([(sr, sc, 0)])
    seen = {(sr, sc)}

    while q:
      cr, cc, ct = q.popleft()

      if track[cr][cc] == "E":
        return ct

      for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if (cr + dr, cc + dc) in seen:
          continue

        if track[cr + dr][cc + dc] in ".E":
          q.append((cr + dr, cc + dc, ct + 1))
          seen.add((cr + dr, cc + dc))


  orig_time = simulate()
  cheats = 0

  for r in range(1, rows - 1):
    for c in range(1, cols - 1):
      if track[r][c] == "#":
        track[r][c] = "."
        cheated_time = simulate()
        cheats += cheated_time <= orig_time - 100
        track[r][c] = "#"

  print(cheats)


if __name__ == "__main__":
  main()