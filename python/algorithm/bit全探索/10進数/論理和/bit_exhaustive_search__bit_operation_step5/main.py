

def get_answer(a: int, b: int) -> int:
    return a | b

def main():
    a = int(input())
    b = int(input())

    print(get_answer(a, b))

def test():
    in_a1 = 203
    in_b1 = 666
    expect1 = 731
    assert get_answer(in_a1, in_b1) == expect1

    in_a2 = 103
    in_b2 = 31
    expect2 = 127
    assert get_answer(in_a2, in_b2) == expect2

test()
main()

# Q
# 論理和 (OR) 基礎 2 Python3編（paizaランク D 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/bit_exhaustive_search/bit_exhaustive_search__bit_operation_step5
# 問題文のURLをコピーする
#  チャレンジする言語
# Python3
# 他の言語でチャレンジする
# コードを書いて解いてみる
# 問題
#  下記の問題をプログラミングしてみよう！
# 与えられた二つの整数の論理和 (OR) をとるプログラムを作成してみましょう。

# 10 進数の整数 A_1, A_2 が与えられるので、A_1 と A_2 のビット毎の論理和 (OR) を 10 進数で出力してください。

# 入力される値
# A_1
# A_2

# ・ 1 行目に整数 A_1 が与えられます。
# ・ 2 行目に整数 A_2 が与えられます。
# ・ 入力は合計で 2 行からなり、入力値最終行の末尾に改行が 1 つ入ります。


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# A_1 と A_2 のビット毎の論理和 (OR) をとった結果を 10 進数で出力してください。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 0 ≦ A_1, A_2 < 2^10

# 入力例1
# 203
# 666

# 出力例1
# 731

# 入力例2
# 103
# 31

# 出力例2
# 127