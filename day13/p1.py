import sys
import re


def extract_numbers(line) -> tuple[int, int]:
  X, Y = map(int, re.findall(r"[+=](\d+)", line.split(": ")[1]))
  return X, Y


def solve_equation(AX, AY, BX, BY, C1, C2) -> int:
  for x in range(101):
    for y in range(101):
      if AX * x + BX * y == C1 and AY * x + BY * y == C2:
        return 3 * x + y

  return 0


def main() -> None:
  claws = open(sys.argv[1]).read().split("\n\n")
  tokens = 0

  for claw in claws:
    (AX, AY), (BX, BY), (prizeX, prizeY) = map(extract_numbers, claw.splitlines())
    tokens += solve_equation(AX, AY, BX, BY, prizeX, prizeY)

  print(tokens)


if __name__ == "__main__":
  main()