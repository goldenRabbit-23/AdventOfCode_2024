import sys
from collections import defaultdict
from itertools import combinations


def main() -> None:
  data = open(sys.argv[1]).read().splitlines()
  connections = [tuple(line.split("-")) for line in data]
  network = defaultdict(set)

  for pc1, pc2 in connections:
    network[pc1].add(pc2)
    network[pc2].add(pc1)

  triangles = set()

  for pc in network:
    neighbors = list(network[pc])

    for neigh1, neigh2 in combinations(neighbors, 2):
      if neigh2 in network[neigh1]:
        triangles.add(tuple(sorted([pc, neigh1, neigh2])))

  print(sum(any(item.startswith('t') for item in triangle) for triangle in triangles))


if __name__ == "__main__":
  main()