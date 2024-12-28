import sys
from collections import defaultdict
from itertools import cycle


def main() -> None:
  wires, gates = open(sys.argv[1]).read().split("\n\n")
  wires = {k: int(v) for k, v in [line.split(": ") for line in wires.splitlines()]}
  gates_dict = defaultdict(lambda: [])
  z_count = 0

  for line in gates.splitlines():
    x, y = line.split(" -> ")[0].split(), line.split(" -> ")[1]

    if (x[2], x[0]) in gates_dict:
      gates_dict[(x[2], x[0])].append((x[1], y))
    else:
      gates_dict[(x[0], x[2])].append((x[1], y))

    z_count += y.startswith('z')

  z_outs = [-1 for _ in range(z_count)]
  z_got = 0

  for (in1, in2), ops in cycle(gates_dict.items()):
    if z_got == z_count:
      break

    if in1 in wires and in2 in wires:
      for op, out in ops:
        if out.startswith('z') and out in wires:
          continue

        if op == "AND":
          wires[out] = wires[in1] & wires[in2]
        elif op == "OR":
          wires[out] = wires[in1] | wires[in2]
        elif op == "XOR":
          wires[out] = wires[in1] ^ wires[in2]

        if out.startswith('z'):
          z_outs[int(out[1:])] = wires[out]
          z_got += 1

  print(int("".join(map(str, reversed(z_outs))), 2))


if __name__ == "__main__":
  main()