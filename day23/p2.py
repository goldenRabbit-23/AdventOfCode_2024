import sys
from collections import defaultdict


def bron_kerbosch(network, r, p, x, max_clique) -> None:
  if len(p) == 0 and len(x) == 0:
    if (len(r) > len(max_clique[0])):
      max_clique[0] = r
    return

  pivot_vertex = max(p | x, key=lambda v: len(network[v] & p))

  for v in p - network[pivot_vertex]:
    neighbors = network[v]
    bron_kerbosch(network, r | {v}, p & neighbors, x & neighbors, max_clique)
    p = p - {v}
    x = x | {v}


def main() -> None:
  data = open(sys.argv[1]).read().splitlines()
  connections = [tuple(line.split("-")) for line in data]
  network = defaultdict(set)

  for pc1, pc2 in connections:
    network[pc1].add(pc2)
    network[pc2].add(pc1)

  # Find maximum clique
  vertices = set(network.keys())
  max_clique = [set()]
  bron_kerbosch(network, set(), vertices, set(), max_clique)

  print(",".join(sorted(max_clique[0])))


if __name__ == "__main__":
  main()