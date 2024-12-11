import sys
from math import log10
from functools import cache


@cache
def blink(stone, level) -> int:
  if level == 0:
    # Base case: each stone contributes a count of 1
    return 1

  if stone == 0:
    # When stone is 0, it transforms to 1 without changing the count
    return blink(1, level - 1)
  elif (d := int(log10(stone)) + 1) % 2 == 0:
    # For numbers with even digit count, split into two equal halves
    # Example: 1234 -> 12 and 34, then process each half recursively
    return blink(stone // (10 ** (d // 2)), level - 1) + \
           blink(stone % (10 ** (d // 2)), level - 1)
  else:
    # For numbers with odd digit count, multiply by 2024
    # The count remains unchanged as this is a 1-to-1 transformation
    return blink(stone * 2024, level - 1)


def main() -> None:
  stones = [int(num) for num in open(sys.argv[1]).read().split()]

  # Calculate and print sum of all stone transformations after 75 levels
  print(sum(blink(stone, 75) for stone in stones))


if __name__ == "__main__":
  main()