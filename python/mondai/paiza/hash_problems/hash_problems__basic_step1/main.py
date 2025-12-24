from typing import List

def get_answer(xs: List[int], a: int, b: int, m: int) -> List[int]:
    ans: List[int] = []
    for i in xs:
        res = ((a * i) + b) % m
        ans.append(res)

    return ans
        

def main():
    n, a, b, m = map(int, input().split())
    xs = [int(input()) for _ in range(n)]
    ans = get_answer(xs, a, b, m)

    for i in ans:
        print(i)
    
def test():
    in_x1 = [
        12,
        9,
        1,
        3,
        7,
    ]
    in_a1 = 3
    in_b1 = 4
    in_mod1 = 7

    expect1 = [
        5,
        3,
        0,
        6,
        4,
    ]

    assert get_answer(in_x1, in_a1, in_b1, in_mod1) == expect1

test()
main()

# Q
# やや複雑なハッシュ Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/hash_problems/hash_problems__basic_step1
# 問題文のURLをコピーする
#  チャレンジする言語
# Python3
# 他の言語でチャレンジする
# コードを書いて解いてみる
# 問題
#  下記の問題をプログラミングしてみよう！
# 前問で実装したハッシュは、とてもシンプルなものでした。本問では、やや複雑なハッシュを計算してみましょう。

# n 個の整数 x_1, x_2, ..., x_n と、整数 a, b, mod が与えられます。各 x_i について、以下のハッシュ関数を用いてハッシュ値を計算してください。


# H(x) = (a * x + b) % mod
# 入力される値
# n a b mod
# x_1
# x_2
# ...
# x_n

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# n 行出力してください。i (1 ≦ i ≦ n) 行目には、x_i のハッシュ値 H(x_i) を出力してください。
# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。


# H(x_1)
# H(x_2)
# ...
# H(x_n)
# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 入力値はすべて整数
# ・ 1 ≦ n ≦ 100
# ・ 1 ≦ a ≦ 10,000
# ・ 1 ≦ b ≦ 10,000
# ・ 2 ≦ mod ≦ 10,000
# ・ 1 ≦ x_i ≦ 10,000 (1 ≦ i ≦ n)

# 入力例1
# 5 3 4 7
# 12
# 9
# 1
# 3
# 7

# 出力例1
# 5
# 3
# 0
# 6
# 4