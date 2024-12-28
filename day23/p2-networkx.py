import sys
import networkx as nx


def main() -> None:
  data = open(sys.argv[1]).read().splitlines()
  connections = [tuple(line.split("-")) for line in data]

  G = nx.Graph()
  G.add_edges_from(connections)
  cliques = nx.find_cliques(G)
  maximum_clique = max(cliques, key=lambda clq: len(clq))
  print(",".join(sorted(maximum_clique)))


if __name__ == "__main__":
  main()