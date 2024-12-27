import sys


def main() -> None:
  track = open(sys.argv[1]).read().splitlines()

  for r, row in enumerate(track):
    for c, ch in enumerate(row):
      if ch == "S":
        sr, sc = r, c

  path = [None, (sr, sc)]
  cr, cc = sr, sc

  while track[cr][cc] != "E":
    cr, cc = path[-1]

    for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
      if track[nr][nc] == "#":
        continue

      if (nr, nc) != path[-2]:
        path.append((nr, nc))
        break

  path = path[1:]
  cheats = 0

  for t1, (r1, c1) in enumerate(path):
    for t2 in range(t1 + 4, len(path)):
      r2, c2 = path[t2]
      dist = abs(r1 - r2) + abs(c1 - c2)
      saved = t2 - t1 - dist
      cheats += dist <= 20 and saved >= 100

  print(cheats)


if __name__ == "__main__":
  main()