import sys
import re


def extract_numbers(line) -> tuple[int, int]:
  X, Y = map(int, re.findall(r"[+=](\d+)", line.split(": ")[1]))
  return X, Y


def solve_equation(AX, AY, BX, BY, C1, C2) -> int:
  X = (BY * C1 - BX * C2) // (AX * BY - AY * BX)
  X_mod = (BY * C1 - BX * C2) % (AX * BY - AY * BX)
  Y = (AX * C2 - AY * C1) // (AX * BY - AY * BX)
  Y_mod = (AX * C2 - AY * C1) % (AX * BY - AY * BX)

  if X_mod == 0 and Y_mod == 0:
    return 3 * X + Y

  return 0


def main() -> None:
  claws = open(sys.argv[1]).read().split("\n\n")
  tokens = 0

  for claw in claws:
    (AX, AY), (BX, BY), (prizeX, prizeY) = map(extract_numbers, claw.splitlines())
    tokens += solve_equation(AX, AY, BX, BY, prizeX + int(1e13), prizeY + int(1e13))

  print(tokens)


if __name__ == "__main__":
  main()