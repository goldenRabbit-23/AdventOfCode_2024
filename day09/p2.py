import sys


def main() -> None:
  disk = list(open(sys.argv[1]).read())
  blocks = []
  files = {}   # {ID: (file_ptr_start, file_count)}
  spaces = []  # (space_ptr_start, space_count)
  cur_id = 0
  cur_file_ptr = 0
  cur_space_ptr = 0

  for i, num in enumerate(disk):
    if i % 2 == 1:
      # free space
      blocks.extend('.' * int(num))
      spaces.append((cur_space_ptr, int(num)))
    else:
      # file
      blocks.extend([str(cur_id)] * int(num))
      files[str(cur_id)] = (cur_file_ptr, int(num))
      cur_id += 1

    cur_file_ptr += int(num)
    cur_space_ptr += int(num)


  def find_space(file_ptr_start, file_count) -> int:
    for i, (space_ptr_start, space_count) in enumerate(spaces):
      if space_ptr_start > file_ptr_start:
        return -1

      if space_count >= file_count:
        return i

    return -1


  for _, (file_ptr_start, file_count) in reversed(list(files.items())):
    found_space_ptr = find_space(file_ptr_start, file_count)

    if found_space_ptr == -1:
      continue

    for i in range(file_count):
      blocks[spaces[found_space_ptr][0] + i], blocks[file_ptr_start + i] = \
        blocks[file_ptr_start + i], blocks[spaces[found_space_ptr][0] + i]

    spaces[found_space_ptr] = \
      (spaces[found_space_ptr][0] + file_count, spaces[found_space_ptr][1] - file_count)

  checksum = 0

  for pos, file in enumerate(blocks):
    if file == '.':
      continue

    checksum += pos * int(file)

  print(checksum)


if __name__ == "__main__":
  main()