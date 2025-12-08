from collections import defaultdict
from typing import List, Dict, Tuple

# ------------------------
# を返却
# ------------------------
def get_answer(a: List[int]) -> int:
    n = len(a)
    dp = [1] * (n)

    for i in range(1, n):
        for j in range(0, i):
            if a[j] > a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp[:])


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
    answer1 = 4
    a = [
        109,
        110,
        108,
        103,
        100,
    ]
    assert get_answer(a) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 【部分列】最長減少部分列 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_boss
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# n 本の木が横一列に並んでいます。左から i 番目の木を木 i と呼ぶことにします。木 i の高さは a_i [cm] です。

# あなたは、何本かの木を伐採することによって、残った木を左から順に見ると高さが単調減少になっているようにしたいと考えています。つまり、残った木を左から 木 k_1, 木 k_2, ... , 木 k_m とすると、a_{k_1} > a_{k_2} > ... > a_{k_m} が満たされているようにしたいです。なるべく多くの木が残るように工夫して伐採する木を選んだとき、伐採されずに残る木の本数が最大でいくつになるか求めてください。

# なお、最初から n 本の木が単調減少に並んでいる場合は、1本も伐採しなくてよいものとします。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# n
# a_1
# a_2
# ...
# a_n


# ・ 1行目に、横一列に並んでいる木の本数 n が与えられます。

# ・ 続く n 行のうち i 行目では、木 i の高さ a_i が与えられます。


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# 残った木を左から見ると高さが単調減少になっているように木を伐採したとき、伐採されずに残る木の本数の最大値を出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 5,000

# ・ 1 ≦ a_i ≦ 1,000,000,000

# ・ a_i ≠ a_j (i ≠ j)

# 入力例1
# 5
# 109
# 110
# 108
# 103
# 100

# 出力例1
# 4