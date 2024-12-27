import sys
from collections import deque

W = 71
H = 71
MAX = 1024


def in_bound(r, c) -> bool:
  return 0 <= r < H and 0 <= c < W


def main() -> None:
  data = [(int(nums[0]), int(nums[1])) for nums in
          [line.split(",") for line in open(sys.argv[1]).read().splitlines()]]
  grid = [["." for _ in range(W)] for _ in range(H)]

  for i, (x, y) in enumerate(data):
    if i >= MAX:  # first `MAX` bytes
      break

    grid[y][x] = "#"

  q = deque([(0, 0, 0)])
  seen = {(0, 0)}
  ans = float("inf")

  while q:
    cr, cc, cs = q.popleft()

    if (cr, cc) == (W - 1, H - 1):
      ans = cs

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
      if not in_bound(cr + dr, cc + dc) or \
         (cr + dr, cc + dc) in seen or \
         grid[cr + dr][cc + dc] == "#":
        continue

      q.append((cr + dr, cc + dc, cs + 1))
      seen.add((cr + dr, cc + dc))

  print(ans)


if __name__ == "__main__":
  main()