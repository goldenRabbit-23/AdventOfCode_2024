import sys
import networkx as nx
from itertools import combinations


def main() -> None:
  data = open(sys.argv[1]).read().splitlines()
  connections = [tuple(line.split("-")) for line in data]

  G = nx.Graph()
  G.add_edges_from(connections)
  cliques = nx.find_cliques(G)
  cliques3 = sorted(set(sum([list(combinations(sorted(clq), 3)) for clq in cliques if len(clq) >= 3], [])))
  print(sum(any(item.startswith('t') for item in clq) for clq in cliques3))


if __name__ == "__main__":
  main()