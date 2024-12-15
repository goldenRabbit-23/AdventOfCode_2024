import sys
from collections import deque


EXPANSION = {"#": "##", "O": "[]", ".": "..", "@": "@."}


def print_grid(grid) -> None:
  for row in grid:
    print(*row, sep="")


def step_horizontal(grid, cr, cc, dc) -> bool:
  # If next space is empty, make the move
  if grid[cr][cc + dc] == ".":
    grid[cr][cc], grid[cr][cc + dc] = grid[cr][cc + dc], grid[cr][cc]
    return True
  # If next space is wall, movement is blocked
  elif grid[cr][cc + dc] == "#":
    return False

  # Recursively try to push connected elements
  if step_horizontal(grid, cr, cc + dc, dc):
    grid[cr][cc], grid[cr][cc + dc] = grid[cr][cc + dc], grid[cr][cc]
    return True

  return False


def can_move_vertical(grid, sr, sc, dr, visited) -> bool:
  q = deque([(sr, sc)])
  visited.append((sr, sc))

  while q:
    cr, cc = q.popleft()

    # Handle box brackets - check connected components
    if grid[cr][cc] == "[" and (cr, cc + 1) not in visited:
      q.append((cr, cc + 1))
      visited.append((cr, cc + 1))
    elif grid[cr][cc] == "]" and (cr, cc - 1) not in visited:
      q.append((cr, cc - 1))
      visited.append((cr, cc - 1))

    # Check cell below/above based on movement direction
    if grid[cr + dr][cc] == ".":
      continue
    elif grid[cr + dr][cc] == "#":
      return False

    if (cr + dr, cc) not in visited:
      q.append((cr + dr, cc))
      visited.append((cr + dr, cc))

  return True


def step_vertical(grid, cr, cc, dr) -> bool:
  visited = []

  if can_move_vertical(grid, cr, cc, dr, visited):
    # Sort visited positions based on movement direction to prevent overlap
    visited.sort(reverse=True if dr == 1 else False)

    # Move all connected components
    for r, c in visited:
      grid[r][c], grid[r + dr][c] = grid[r + dr][c], grid[r][c]
    return True

  return False


def main() -> None:
  grid, moves = open(sys.argv[1]).read().split("\n\n")
  ngrid = [list("".join(EXPANSION[ch] for ch in row)) for row in grid.splitlines()]
  moves = moves.replace("\n", "")

  for r, row in enumerate(ngrid):
    for c, ch in enumerate(row):
      if ch == "@":
        rr, rc = r, c

  for move in moves:
    if move == "<":
      if step_horizontal(ngrid, rr, rc, -1):
        rc -= 1
    elif move == ">":
      if step_horizontal(ngrid, rr, rc, 1):
        rc += 1
    elif move == "^":
      if step_vertical(ngrid, rr, rc, -1):
        rr -= 1
    elif move == "v":
      if step_vertical(ngrid, rr, rc, 1):
        rr += 1

  gps = 0

  for r, row in enumerate(ngrid):
    for c, ch in enumerate(row):
      if ch == "[":
        gps += 100 * r + c

  # print_grid(ngrid)
  print(gps)


if __name__ == "__main__":
  main()