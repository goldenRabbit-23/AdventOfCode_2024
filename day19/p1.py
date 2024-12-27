import sys
from functools import cache


@cache
def can_make(target, available) -> bool:
  if target == "":
    return True

  for towel in available:
    if len(towel) > len(target):
      continue

    if target[:len(towel)] != towel:
      continue

    if can_make(target[len(towel):], available):
      return True

  return False


def main() -> None:
  towels, designs = open(sys.argv[1]).read().split("\n\n")
  towels = tuple(towels.split(", "))
  designs = designs.splitlines()

  ans = 0

  for design in designs:
    ans += can_make(design, towels)

  print(ans)


if __name__ == "__main__":
  main()