import sys
from collections import defaultdict


def main() -> None:
  orderings, updates = open(sys.argv[1]).read().split("\n\n")
  orderings = [tuple(map(int, ordering.split("|"))) for ordering in orderings.splitlines()]
  updates = [list(map(int, update.split(","))) for update in updates.splitlines()]
  ordering_dict = defaultdict(list[int])

  for fst, snd in orderings:
    ordering_dict[fst].append(snd)

  def correct_order(update) -> bool:
    for i in range(len(update) - 1):
      for j in range(i+1, len(update)):
        if update[i] not in ordering_dict or update[j] not in ordering_dict[update[i]]:
          return False

    return True

  result = 0

  for update in updates:
    if correct_order(update):
      result += update[len(update) // 2]

  print(result)


if __name__ == "__main__":
  main()