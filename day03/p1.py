import sys
import re


def main() -> None:
  lines = open(sys.argv[1]).read().splitlines()
  pattern = r"mul\((\d+),(\d+)\)"
  result = 0

  for line in lines:
    matches = re.findall(pattern, line)

    for x, y in matches:
      result += int(x) * int(y)

  print(result)


if __name__ == "__main__":
  main()