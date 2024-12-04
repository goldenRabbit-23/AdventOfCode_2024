import sys


def main() -> None:
  grid = open(sys.argv[1]).read().splitlines()
  rows, columns = len(grid), len(grid[0])
  count = 0

  for r in range(rows):
    for c in range(columns):
      valid_1 = False  # \ direction
      valid_2 = False  # / direction

      # skip all sides
      if r == 0 or r == rows - 1 or c == 0 or c == columns - 1:
        continue

      # search for center of X
      if grid[r][c] != "A":
        continue

      # 'MAS' in \ direction
      if grid[r-1][c-1] + grid[r+1][c+1] in ["MS", "SM"]:
        valid_1 = True

      # 'MAS' in / direction
      if grid[r-1][c+1] + grid[r+1][c-1] in ["MS", "SM"]:
        valid_2 = True

      # X-MAS
      if valid_1 and valid_2:
        count += 1

  print(count)


if __name__ == "__main__":
  main()