import sys
from collections import deque


def hash_delta(a, b, c, d) -> int:
  return (a + 9) + (b + 9) * 19 + (c + 9) * 19 * 19 + (d + 9) * 19 * 19 * 19


def main() -> None:
  secrets = list(map(int, open(sys.argv[1]).read().splitlines()))
  bananas = [0 for _ in range(19 ** 4)]

  for i, secret in enumerate(secrets):
    seen = set()
    changes = deque(maxlen=4)

    for it in range(2000):
      secret = ((secret << 6) ^ secret) & 0xffffff
      secret = ((secret >> 5) ^ secret) & 0xffffff
      secret = ((secret << 11) ^ secret) & 0xffffff

      changes.append(secret % 10 - secrets[i] % 10)

      if it >= 3:
        hashed_delta = hash_delta(*changes)

        if hashed_delta not in seen:
          bananas[hashed_delta] += secret % 10
          seen.add(hashed_delta)

      secrets[i] = secret

  print(max(bananas))


if __name__ == "__main__":
  main()