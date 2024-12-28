import sys


def main() -> None:
  secrets = list(map(int, open(sys.argv[1]).read().splitlines()))

  for _ in range(2000):
    for i, secret in enumerate(secrets):
      secret = ((secret << 6) ^ secret) & 0xffffff
      secret = ((secret >> 5) ^ secret) & 0xffffff
      secret = ((secret << 11) ^ secret) & 0xffffff
      secrets[i] = secret

  print(sum(secrets))


if __name__ == "__main__":
  main()