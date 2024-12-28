import sys


def B(A) -> int:  # hard-coded
  return (((A % 8 ^ 7) ^ (A >> (A % 8 ^ 7))) ^ 4) % 8


def backtrack(modulos, candidate) -> int | float:
  if modulos == []:
    return candidate

  candidates = [
    backtrack(modulos[1:], next_candidate)
    for next_candidate in range(candidate * 8, candidate * 8 + 8)
    if B(next_candidate) == modulos[0]
  ]

  return min(candidates) if candidates else float("inf")


def main() -> None:
  prog = open(sys.argv[1]).read().split("\n\n")[1]
  prog = list(map(int, prog.split(": ")[1].split(",")))

  print(backtrack(prog[::-1], 0))


if __name__ == "__main__":
  main()