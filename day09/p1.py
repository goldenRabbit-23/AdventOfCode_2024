import sys


def main() -> None:
  disk = list(open(sys.argv[1]).read())
  blocks = []
  cur_id = 0

  for i, num in enumerate(disk):
    if i % 2 == 1:
      # free space
      blocks.extend('.' * int(num))
    else:
      # file
      blocks.extend([str(cur_id)] * int(num))
      cur_id += 1

  # defrag
  space_ptr = int(disk[0])
  last_ptr = len(blocks) - 1

  while space_ptr <= last_ptr:
    blocks[space_ptr], blocks[last_ptr] = blocks[last_ptr], blocks[space_ptr]

    # find next free space
    space_ptr += 1
    while blocks[space_ptr] != '.':
      space_ptr += 1

    # find prev file
    last_ptr -= 1
    while blocks[last_ptr] == '.':
      last_ptr -= 1

  checksum = 0

  for pos, file in enumerate(blocks):
    if file == '.':
      break

    checksum += pos * int(file)

  print(checksum)


if __name__ == "__main__":
  main()