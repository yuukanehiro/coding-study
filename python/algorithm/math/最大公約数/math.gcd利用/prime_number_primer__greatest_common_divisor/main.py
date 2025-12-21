from math import gcd
from typing import List

# ------------------------
# 最大公約数を返却
# ------------------------
def get_answer(a: List[int]) -> int:
    ans = 0
    for v in a:
        ans = gcd(ans, v)
    
    return ans

def main():
    # item_count, query_count = map(int, input().split())
    # n = int(input()) # 1つのintの場合
    # inputList = list(map(int, input().split()))
    # item_count, query_count = inputList[0], inputList[1]
    # items = [input().strip() for _ in range(item_count)]

    # n回のList[int]
    # n = int(input())
    # heights = [int(input()) for _ in range(n)]

    # 2次元配列
    # items = [list(map(int, input().split())) for _ in range(item_count)]
    # 1 - indexed
    # items = [0] + [int(input().strip()) for _ in range(item_count)]
    # queries = [input().strip() for _ in range(query_count)]
    # queries: Dict[int, str] = {int(line.split()[0]): line.split()[1] for line in (input().strip() for _ in range(query_count))}
    # queries: List[Tuple[int, str]] = [(int(line.split()[0]), line.split()[1]) for line in (input().strip() for _ in range(query_count))]

    n = int(input())
    a = [int(input()) for _ in range(n)]
    print(get_answer(a))


# ------------------------
# テストコード
# ------------------------
def test():
    in1 = [
        2,
        6,
        8,
    ]
    answer1 = 2
    assert get_answer(in1) == answer1

    in2 = [
        4,
        7,
        14,
        35,
        60,
    ]
    answer2 = 1
    assert get_answer(in2) == answer2

if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 最大公約数 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__greatest_common_divisor
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 複数個の整数に共通する約数のうち、最大のものを最大公約数といいます。
# 整数 N と N 個の整数 A_1 , ... , A_N が与えられるので、A_1 , ... , A_N の最大公約数を求めてください。
# なお、最大公約数は、「全ての整数に共通する素因数の{最小の指数}乗」の積となることが知られています。
# 例として、12 , 30 , 81 の最大公約数は、 12 = 2^2 × 3^1 × 5^0 , 30 = 2^1 × 3^1 × 5^1 , 81 = 2^0 × 3^4 × 5^0 より、素因数 2 についての乗数の最小値は 0 , 素因数 3 についての乗数の最小値は 1 , 素因数 5 についての乗数の最小値は 0 であるため、最大公約数は 2^0 × 3^1 × 5^0 = 3 となります。

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
# ・ A_1 , ... , A_N の最大公約数を 1 行で出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ・ 1 ≦ N ≦ 1,000
# ・ 1 ≦ A_i ≦ 100,000 (1 ≦ i ≦ N)

# 入力例1
# 2
# 6
# 8

# 出力例1
# 2

# 入力例2
# 4
# 7
# 14
# 35
# 60

# 出力例2
# 1