import sys
import re


W = 101
H = 103


def print_grid(robots) -> None:
  for y in range(H):
    for x in range(W):
      if (x, y) in robots:
        print("*", end="")
      else:
        print(".", end="")
    print()


def maybe_christmas_tree(robots) -> bool:
  total = len(robots)
  count = 0

  for x, y in robots:
    count += any((x + dx, y + dy) in robots
                  for dx, dy
                  in [(-1, 0), (0, -1), (1, 0), (0, 1)])

  return count >= total // 2


def main() -> None:
  data = open(sys.argv[1]).read().splitlines()
  robots = []
  velocity = []

  for line in data:
    p, v = re.findall(r"(-*\d+),(-*\d+)", line)
    robots.append((int(p[0]), int(p[1])))
    velocity.append((int(v[0]), int(v[1])))

  second = 0

  while True:
    for i, ((p1, p2), (v1, v2)) in enumerate(zip(robots, velocity)):
      robots[i] = ((p1 + v1) % W, (p2 + v2) % H)

    second += 1

    if maybe_christmas_tree(robots):
      break

  print_grid(robots)
  print(second)


if __name__ == "__main__":
  main()