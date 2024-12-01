import sys
from collections import Counter


def main() -> None:
  lines = open(sys.argv[1]).read().splitlines()
  column1 = []
  column2 = []
  score = 0

  for line in lines:
    numbers = line.split()
    column1.append(int(numbers[0]))
    column2.append(int(numbers[1]))

  counter = Counter(column2)

  for x in column1:
    score += x * counter[x]

  print(score)


if __name__ == "__main__":
  main()