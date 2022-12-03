from collections import defaultdict

def prime_factorize(N):
  # 答えを表す可変長配列
  res = defaultdict(int)

  # √N まで試し割っていく
  for p in range(2, N):
    # p * p <= N の範囲でよい
    if p * p > N:
      break

    # N が p で割り切れないならばスキップ
    if N % p != 0:
      continue

    # N の素因数 p に対する指数を求める
    e = 0
    while N % p == 0:
      # 指数を 1 増やす
      e += 1

      # N を p で割る
      N //= p

    # 答えに追加
    res[p]=e

  # 素数が最後に残ることがありうる
  if N != 1:
    res[N]=1

  return res

def progress(value):
  if value == 1:
    return 1
  else:
    i=2
    while value>i*(1+i)/2:
      i+=1
    return i

def main():
  maximum = 0
  K = int(input())
  pf1 = prime_factorize(K)
  for key, value in pf1.items():
    maximum = max(maximum, key**progress(value))
  print(maximum)

if __name__ == '__main__':
  main()