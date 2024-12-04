import sys


def main() -> None:
  grid = open(sys.argv[1]).read().splitlines()
  rows, columns = len(grid), len(grid[0])
  count = 0

  for r in range(rows):
    for c in range(columns):
      # E
      if c <= columns - 4 and grid[r][c:c+4] in ["XMAS", "SAMX"]:
        count += 1

      # SE
      if r <= rows - 4 and c <= columns - 4:
        if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] + grid[r+3][c+3] in ["XMAS", "SAMX"]:
          count += 1

      # S
      if r <= rows - 4:
        if grid[r][c] + grid[r+1][c] + grid[r+2][c] + grid[r+3][c] in ["XMAS", "SAMX"]:
          count += 1

      # SW
      if r <= rows - 4 and c >= 3:
        if grid[r][c] + grid[r+1][c-1] + grid[r+2][c-2] + grid[r+3][c-3] in ["XMAS", "SAMX"]:
          count += 1

  print(count)


if __name__ == "__main__":
  main()