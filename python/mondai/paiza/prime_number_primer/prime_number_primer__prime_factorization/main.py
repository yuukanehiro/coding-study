
from typing import List

# ------------------------
# を返却
# ------------------------
def get_answer(n: int) -> List[int]:
    primers: List[int] = []

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            primers.append(i)
            n //= i

    # 重要: ループを抜けたとき、もし n が 1 より大きければ、その n は素因数
    if n != 1:
        primers.append(n)

    return primers


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
    a = get_answer(n)
    for v in a:
        print(v)


# ------------------------
# テストコード
# ------------------------
def test():
    in1 = 8
    answer1 = [
        2,
        2,
        2,
    ]
    assert get_answer(in1) == answer1

    in2 = 174
    answer2 = [
        2,
        3,
        29,
    ]
    assert get_answer(in2) == answer2


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 素因数分解 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__prime_factorization
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# ある整数を素数の積の形で表現することを素因数分解といいます。
# 例として、15 を素因数分解すると 3 × 5 となり、11 を素因数分解すると 11 となり、 16 を素因数分解すると 2 × 2 × 2 × 2 となります。
# 整数 N が与えられるので、N を素因数分解してみましょう。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# N


# ・ 1 行で整数 N が与えられます。

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# N を素因数分解したときに現れる素数を小さい方から順に改行区切りで出力してください。
# 同じ素数が複数回現れる場合は、現れる回数だけその素数を出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ・ 2 ≦ N ≦ 100,000

# 入力例1
# 8

# 出力例1
# 2
# 2
# 2

# 入力例2
# 174

# 出力例2
# 2
# 3
# 29