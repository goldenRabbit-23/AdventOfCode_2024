import sys
from collections import defaultdict, deque


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

  incorrect_updates = []

  # find updates with an incorrect order
  for update in updates:
    if not correct_order(update):
      incorrect_updates.append(update)

  result = 0

  # part 2
  for incorrect_update in incorrect_updates:
    # compute new subgraph and indegrees for each incorrect update
    subgraph = defaultdict(list[int])
    indegree = defaultdict(int)

    for fst, snd in orderings:
      if all(x in incorrect_update for x in [fst, snd]):
        subgraph[fst].append(snd)

        if fst not in indegree:
          indegree[fst] = 0
        indegree[snd] += 1

    corrected = []
    q = deque()

    for page, ind in indegree.items():
      if ind == 0:
        q.append(page)

    # start from source
    while q:
      now = q.popleft()
      corrected.append(now)

      for page in subgraph[now]:
        indegree[page] -= 1

        if indegree[page] == 0:
          q.append(page)

    result += corrected[len(corrected) // 2]

  print(result)


if __name__ == "__main__":
  main()