import sys


def main() -> None:
  lines = open(sys.argv[1]).read().splitlines()
  column1 = []
  column2 = []
  dist = 0

  for line in lines:
    numbers = line.split()
    column1.append(int(numbers[0]))
    column2.append(int(numbers[1]))

  column1.sort()
  column2.sort()

  for x, y in zip(column1, column2):
    dist += abs(x - y)

  print(dist)


if __name__ == "__main__":
  main()