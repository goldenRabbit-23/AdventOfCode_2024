import sys


def print_grid(grid) -> None:
  for row in grid:
    print(*row, sep="")


def step(grid, cr, cc, dr, dc) -> bool:
  if grid[cr + dr][cc + dc] == ".":
    grid[cr][cc], grid[cr + dr][cc + dc] = grid[cr + dr][cc + dc], grid[cr][cc]
    return True
  elif grid[cr + dr][cc + dc] == "#":
    return False

  if step(grid, cr + dr, cc + dc, dr, dc):
    grid[cr][cc], grid[cr + dr][cc + dc] = grid[cr + dr][cc + dc], grid[cr][cc]
    return True

  return False


def main() -> None:
  grid, moves = open(sys.argv[1]).read().split("\n\n")
  grid = list(map(list, grid.splitlines()))
  moves = moves.replace("\n", "")

  for r, row in enumerate(grid):
    for c, ch in enumerate(row):
      if ch == "@":
        rr, rc = r, c

  for move in moves:
    if move == "^":
      if step(grid, rr, rc, -1, 0):
        rr -= 1
    elif move == ">":
      if step(grid, rr, rc, 0, 1):
        rc += 1
    elif move == "v":
      if step(grid, rr, rc, 1, 0):
        rr += 1
    elif move == "<":
      if step(grid, rr, rc, 0, -1):
        rc -= 1

  gps = 0

  for r, row in enumerate(grid):
    for c, ch in enumerate(row):
      if ch == "O":
        gps += 100 * r + c

  # print_grid(grid)
  print(gps)


if __name__ == "__main__":
  main()