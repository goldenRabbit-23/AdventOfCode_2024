import sys


def main() -> None:
  gates_str = open(sys.argv[1]).read().split("\n\n")[1]
  gates = []
  z_msb = 0

  for line in gates_str.splitlines():
    (in1, op, in2), out = line.split(" -> ")[0].split(), line.split(" -> ")[1]
    gates.append((in1, op, in2, out))
    z_msb = max(z_msb, int(out[1:]) if out.startswith("z") else 0)

  bad_wires = []

  for in1, op, _, out in gates:
    if in1 in ("x00", "y00") or out == f"z{z_msb}": continue

    in_c, out_c = in1.startswith(("x", "y")), out.startswith("z")

    if ((op != "XOR" or in_c) and out_c) or (op == "XOR" and (not (in_c or out_c) or
      any(out in (i, j) and o == "OR" for i, o, j, _ in gates))) or (op == "AND" and
      any(out in (i, j) and o != "OR" for i, o, j, _ in gates)): bad_wires.append(out)

  print(",".join(sorted(bad_wires)))


if __name__ == "__main__":
  main()