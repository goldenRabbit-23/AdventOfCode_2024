import sys
from collections import deque


def main() -> None:
  grid = open(sys.argv[1]).read().splitlines()
  rows, cols = len(grid), len(grid[0])
  visited = [[False for _ in range(cols)] for _ in range(rows)]


  def in_bound(r, c) -> bool:
    return 0 <= r < rows and 0 <= c < cols


  def is_same_type(r, c, plot_type) -> bool:
    return in_bound(r, c) and grid[r][c] == plot_type


  def traverse(sr, sc, plot_type) -> tuple[int, int]:
    area = 0
    corners = 0
    q = deque([(sr, sc)])

    # Directions: N, E, S, W
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
      cr, cc = q.popleft()

      if visited[cr][cc]:
        continue

      visited[cr][cc] = True
      area += 1

      # Pre-compute adjacent cell types for cleaner corner checking
      adjacent = [is_same_type(cr + dr, cc + dc, plot_type) for dr, dc in DIRS]
      N, E, S, W = adjacent

      # Exterior corners - when two adjacent sides are different type or out of bounds
      corner_pairs = [(N, E), (S, E), (S, W), (N, W)]
      corners += sum(1 for side1, side2 in corner_pairs if not side1 and not side2)

      # Interior corners - when two adjacent sides are same type but diagonal is different
      if N and E and not is_same_type(cr - 1, cc + 1, plot_type):
        corners += 1
      if S and E and not is_same_type(cr + 1, cc + 1, plot_type):
        corners += 1
      if S and W and not is_same_type(cr + 1, cc - 1, plot_type):
        corners += 1
      if N and W and not is_same_type(cr - 1, cc - 1, plot_type):
        corners += 1

      # Add unvisited neighbors of same type to queue
      for i, (dr, dc) in enumerate(DIRS):
        if adjacent[i]:
          nr, nc = cr + dr, cc + dc
          q.append((nr, nc))

    return area, corners


  price = 0

  for r, row in enumerate(grid):
    for c, plot in enumerate(row):
      if not visited[r][c]:
        area, corners = traverse(r, c, plot)
        price += area * corners

  print(price)


if __name__ == "__main__":
  main()