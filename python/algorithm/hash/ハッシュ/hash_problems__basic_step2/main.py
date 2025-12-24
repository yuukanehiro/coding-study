from typing import List

def get_answer(xs: List[str]) -> List[int]:
    ans: List[int] = []

    for x in xs:
        s = x.count('p') + x.count('a') + x.count('i') + x.count('z')
        ans.append(s)

    return ans

def main():
    n = int(input())
    a = [input() for _ in range(n)]

    ans = get_answer(a)
    for i in ans:
        print(i)

def test():
    in1 = [
        "paiza",
        "pizza",
        "kirishima",
        "aizap",
        "neko",
    ]
    expect1 = [
        5,
        5,
        4,
        5,
        0,
    ]
    assert get_answer(in1) == expect1

test()
main()

# Q
# 文字列のハッシュ Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/hash_problems/hash_problems__basic_step2
# 問題文のURLをコピーする
#  チャレンジする言語
# Python3
# 他の言語でチャレンジする
# コードを書いて解いてみる
# 問題
#  下記の問題をプログラミングしてみよう！
# 前問までで実装したハッシュは、ともに整数値を入力としてとるものでした。ハッシュの入力として与えられるデータは、整数値に限りません。文字列、オブジェクトなどさまざまです。本問では、文字列を入力とするハッシュ関数を実装してみましょう。

# n 個の文字列 x_1, x_2, ..., x_n が与えられます。各 x_i について、以下のハッシュ関数を用いてハッシュ値を計算してください。


# H(x) = x.count('p') + x.count('a') + x.count('i') + x.count('z')


# なお、文字列 s と文字 c について、s.count(c) は s に含まれる文字 c の個数を表します。
# 入力される値
# n
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

# ・ 1 ≦ n ≦ 100
# ・ x_i (1 ≦ i ≦ n) は、英小文字 a, b, ..., z からなる 1 文字以上 100 文字以下の文字列

# 入力例1
# 5
# paiza
# pizza
# kirishima
# aizap
# neko

# 出力例1
# 5
# 5
# 4
# 5
# 0