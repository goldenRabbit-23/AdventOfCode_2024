import sys


# North, East, South, West
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

def main() -> None:
  grid = open(sys.argv[1]).read().splitlines()
  rows, cols = len(grid), len(grid[0])

  # find starting point
  def find_starting_point() -> tuple[int, int]:
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "^":
          return r, c

  curr, curc = find_starting_point()
  curdir = 0
  positions = set()

  while 0 < curr < rows - 1 and 0 < curc < cols - 1:
    positions.add((curr, curc))
    nr = curr + DR[curdir]
    nc = curc + DC[curdir]

    if grid[nr][nc] in ".^":
      curr, curc = nr, nc
    else:
      curdir = (curdir + 1) % 4
      curr, curc = curr + DR[curdir], curc + DC[curdir]

  positions.add((curr, curc))
  print(len(positions))


if __name__ == "__main__":
  main()