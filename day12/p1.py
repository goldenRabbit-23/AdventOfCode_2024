import sys
from collections import deque


def main() -> None:
  grid = open(sys.argv[1]).read().splitlines()
  rows, cols = len(grid), len(grid[0])
  visited = [[False for _ in range(cols)] for _ in range(rows)]


  def traverse(sr, sc, plot_type) -> tuple[int, int]:
    area = 0
    perimeter = 0
    q = deque([(sr, sc)])

    while q:
      cr, cc = q.popleft()

      if visited[cr][cc]:
        continue

      visited[cr][cc] = True
      area += 1
      # Each plot initially contributes 4 sides to the perimeter
      perimeter += 4

      # Check all four adjacent neighbors (up, right, down, left)
      for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr = cr + dr
        nc = cc + dc

        # Skip if neighbor is outside the grid boundaries
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
          continue

        # When two plots of the same type share an edge, subtract one from the perimeter
        # as the shared edge doesn't contribute to the outer boundary
        if grid[nr][nc] == plot_type:
          perimeter -= 1
          q.append((nr, nc))

    return area, perimeter


  price = 0

  for r, row in enumerate(grid):
    for c, plot in enumerate(row):
      if not visited[r][c]:
        area, perimeter = traverse(r, c, plot)
        price += area * perimeter

  print(price)


if __name__ == "__main__":
  main()