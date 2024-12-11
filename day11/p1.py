import sys
from math import log10


def main() -> None:
  stones = [int(num) for num in open(sys.argv[1]).read().split()]

  for _ in range(25):
    i = 0

    while i < len(stones):
      if stones[i] == 0:
        # engraved with 0
        stones[i] = 1
        i += 1
      elif int(log10(stones[i])) % 2 == 1:
        # even number of digits
        num_str = str(stones[i])
        mid = len(num_str) // 2
        first_half, second_half = int(num_str[:mid]), int(num_str[mid:])
        stones[i] = first_half
        stones.insert(i+1, second_half)
        i += 2
      else:
        stones[i] *= 2024
        i += 1

  print(len(stones))


if __name__ == "__main__":
  main()