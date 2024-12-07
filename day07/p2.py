import sys


def is_valid_eq(answer, numbers, cur_idx, cur_res) -> bool:
  if cur_idx >= len(numbers):
    return answer == cur_res

  return is_valid_eq(answer, numbers, cur_idx + 1, cur_res + numbers[cur_idx]) \
        or is_valid_eq(answer, numbers, cur_idx + 1, cur_res * numbers[cur_idx]) \
        or is_valid_eq(answer, numbers, cur_idx + 1, int(str(cur_res) + str(numbers[cur_idx])))

def main() -> None:
  lines = open(sys.argv[1]).read().splitlines()
  total = 0

  for line in lines:
    answer, *numbers = map(int, line.replace(": ", " ").split())

    if is_valid_eq(answer, numbers, 1, numbers[0]):
      total += answer

  print(total)


if __name__ == "__main__":
  main()