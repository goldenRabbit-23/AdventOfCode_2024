import sys


# North, East, South, West
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

def main() -> None:
  grid = list(map(list, open(sys.argv[1]).read().splitlines()))
  rows, cols = len(grid), len(grid[0])

  # find starting point
  def find_starting_point() -> tuple[int, int]:
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "^":
          return r, c

  sr, sc = find_starting_point()
  visited_cells = set()

  def patrol() -> None:
    curr, curc, curdir = sr, sc, 0

    while 0 < curr < rows - 1 and 0 < curc < cols - 1:
      visited_cells.add((curr, curc))
      nr = curr + DR[curdir]
      nc = curc + DC[curdir]

      if grid[nr][nc] in ".^":
        curr, curc = nr, nc
      else:
        curdir = (curdir + 1) % 4
        curr, curc = curr + DR[curdir], curc + DC[curdir]

    visited_cells.add((curr, curc))

  patrol()

  # True if stuck in a loop, False otherwise
  def stuck_in_a_loop() -> bool:
    curr, curc, curdir = sr, sc, 0
    visited = set()

    while True:
      if (curr, curc, curdir) in visited:
        return True

      visited.add((curr, curc, curdir))
      nr = curr + DR[curdir]
      nc = curc + DC[curdir]

      if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        return False

      if grid[nr][nc] in ".^":
        curr, curc = nr, nc
      else:
        curdir = (curdir + 1) % 4

  positions = 0

  for r in range(rows):
    for c in range(cols):
      if (r, c) not in visited_cells or grid[r][c] == "^":
        continue

      grid[r][c] = "#"
      positions += stuck_in_a_loop()
      grid[r][c] = "."

  print(positions)


if __name__ == "__main__":
  main()