# 素数を高速に発見するアルゴリズム「エラトステネスのふるい」
import sys
import math


def eratosthenes(limit):
  nums = [i for i in range(2, limit+1)]  # 素数の候補
  primes = []  # 素数のリスト

  while True:
    p = min(nums)  # 最小値

    if p > math.sqrt(limit):  # 次の素数がpなら，p^2より小さい数で残ったものはすべて素数であるため探索終了
      break

    primes.append(p)

    i = 0
    while i < len(nums):
      if nums[i] % p == 0:
        nums.pop(i)  # 素数の倍数の数値を候補から外す
      else:
        i += 1

  return primes + nums


def main(argv):
  if not argv[0].isdigit():  # 入力が数値か判定
    print(f"[Error]Invalid argument: {argv[0]}")
    return

  n = int(argv[0])

  if n < 2:
    print("[Error]Input number must be greater than or equal to 2.")
    return

  primes = eratosthenes(n)
  print(primes)  # n以下の素数を表示


if __name__ == '__main__':
  main(sys.argv[1:])