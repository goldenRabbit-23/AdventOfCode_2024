import sys
import re


def main() -> None:
  lines = open(sys.argv[1]).read().splitlines()
  patterns = {
      "mul": r"mul\((\d+),(\d+)\)",
      "do": r"do\(\)",
      "don't": r"don't\(\)"
  }
  result = 0
  enabled = True

  for line in lines:
    matches = []

    for pattern in patterns.values():
      for match in re.finditer(pattern, line):
        matches.append((match.start(), match.group()))

    matches.sort()

    for _, match in matches:
      if match == "do()":
        enabled = True
      elif match == "don't()":
        enabled = False
      elif enabled:
        x, y = re.findall(patterns["mul"], match)[0]
        result += int(x) * int(y)

  print(result)


if __name__ == "__main__":
  main()