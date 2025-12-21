from math import lcm, gcd
from typing import List

# ------------------------
# 最小公倍数を返却
# ------------------------
def get_answer(a: List[int]) -> int:
    current_lcm = a[0]

    for i in range(1, len(a)):
        target = a[i]
        current_lcm = (current_lcm * target) // gcd(current_lcm, target)

    return current_lcm

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    print(get_answer(a))


# ------------------------
# テストコード
# ------------------------
def test():
    # inにNとa1,a2,aNがある場合にNが含めてしまうミスが多いので気をつける
    in1 = [
        10,
        25,
    ]
    answer1 = 50
    assert get_answer(in1) == answer1

    in2 = [
        2,
        3,
        5,
        7,
    ]
    answer2 = 210
    assert get_answer(in2) == answer2

if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 最小公倍数 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__least_common_multiple
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 複数個の整数に共通する倍数のうち、最小のものを最小公倍数といいます。
# 整数 N と N 個の整数 A_1 , ... , A_N が与えられるので、A_1 , ... , A_N の最小公倍数を求めてください。

# なお、最小公倍数は、「全ての整数のうち、いずれかの整数の素因数の{最大の指数}乗」の積になることが知られています。
# 例として、12 , 30 , 81 の最小公倍数は、 12 = 2^2 × 3^1 × 5^0 , 30 = 2^1 × 3^1 × 5^1 , 81 = 2^0 × 3^4 × 5^0 より、素因数 2 についての乗数の最大値は 2 , 素因数 3 についての乗数の最大値は 4 , 素因数 5 についての乗数の最大値は 1 であるため、最小公倍数は 2^2 × 3^4 × 5^1 = 1620 となります。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# N
# A_1
# ...
# A_N


# ・ 1 行目で整数 N が与えられます。
# ・ 続く N 行のうち、 i 行目では整数 A_i が与えられます。(1 ≦ i ≦ N)

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# A_1 ... A_N の最小公倍数を 1 行で出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ・ 1 ≦ N ≦ 100
# ・ 1 ≦ A_i ≦ 100 (1 ≦ i ≦ N)
# ・ 答えは 10^13 以下になることが保証されている。

# 入力例1
# 2
# 10
# 25

# 出力例1
# 50

# 入力例2
# 4
# 2
# 3
# 5
# 7

# 出力例2
# 210