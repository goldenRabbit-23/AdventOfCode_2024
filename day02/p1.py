import sys


def main() -> None:
  lines = open(sys.argv[1]).read().splitlines()
  safe = 0

  for line in lines:
    report = list(map(int, line.split()))
    init_comp = report[0] - report[1]

    if init_comp == 0 or abs(init_comp) > 3:
      continue

    def is_safe() -> bool:
      for x, y in zip(report[1:], report[2:]):
        comp = x - y

        if comp == 0 or abs(comp) > 3 or init_comp * comp < 0:
          return False

      return True

    safe += is_safe()

  print(safe)


if __name__ == "__main__":
  main()