import sys
import re
from math import prod


W = 101
H = 103


def main() -> None:
  data = open(sys.argv[1]).read().splitlines()
  robots = []
  velocity = []

  for line in data:
    p, v = re.findall(r"(-*\d+),(-*\d+)", line)
    robots.append((int(p[0]), int(p[1])))
    velocity.append((int(v[0]), int(v[1])))

  for _ in range(100):
    for i, ((p1, p2), (v1, v2)) in enumerate(zip(robots, velocity)):
      robots[i] = ((p1 + v1) % W, (p2 + v2) % H)

  robots_per_quad = [0, 0, 0, 0]
  mid_W = W // 2
  mid_H = H // 2

  for x, y in robots:
    if x < mid_W and y < mid_H:    # Q1
      robots_per_quad[0] += 1
    elif x > mid_W and y < mid_H:  # Q2
      robots_per_quad[1] += 1
    elif x < mid_W and y > mid_H:  # Q3
      robots_per_quad[2] += 1
    elif x > mid_W and y > mid_H:  # Q4
      robots_per_quad[3] += 1

  print(prod(robots_per_quad))


if __name__ == "__main__":
  main()