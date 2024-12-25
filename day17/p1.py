import sys


def main() -> None:
  regs, prog = open(sys.argv[1]).read().split("\n\n")
  regs = [int(reg.split(": ")[1]) for reg in regs.splitlines()]
  prog = list(map(int, prog.split(": ")[1].split(",")))

  combo = [0, 1, 2, 3, *regs]
  prog_len = len(prog)
  inst_ptr = 0
  output = []

  while inst_ptr < prog_len:
    opcode, operand = prog[inst_ptr], prog[inst_ptr + 1]

    if opcode == 0:
      regs[0] = regs[0] >> combo[operand]
    elif opcode == 1:
      regs[1] = regs[1] ^ operand
    elif opcode == 2:
      regs[1] = combo[operand] % 8
    elif opcode == 3:
      if regs[0] > 0:
        inst_ptr = operand
        continue
    elif opcode == 4:
      regs[1] = regs[1] ^ regs[2]
    elif opcode == 5:
      output.append(combo[operand] % 8)
    elif opcode == 6:
      regs[1] = regs[0] >> combo[operand]
    elif opcode == 7:
      regs[2] = regs[0] >> combo[operand]

    inst_ptr += 2
    combo[4] = regs[0]
    combo[5] = regs[1]
    combo[6] = regs[2]

  print(",".join(map(str, output)))


if __name__ == "__main__":
  main()