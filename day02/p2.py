import sys


def get_sub_reports(original) -> list[list[int]]:
  return [original[:i] + original[i+1:] for i in range(len(original))]

def examine(report) -> bool:
  init_comp = report[0] - report[1]

  if init_comp == 0 or abs(init_comp) > 3:
    return False

  for x, y in zip(report[1:], report[2:]):
    comp = x - y

    if comp == 0 or abs(comp) > 3 or init_comp * comp < 0:
      return False

  return True

def main() -> None:
  lines = open(sys.argv[1]).read().splitlines()
  safe = 0

  for line in lines:
    report = list(map(int, line.split()))

    if examine(report):
      safe += 1
      continue

    if any(examine(sub_report) for sub_report in get_sub_reports(report)):
      safe += 1

  print(safe)


if __name__ == "__main__":
  main()