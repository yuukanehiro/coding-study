
def get_answer(n: int) -> str:
    if n & 1 == 1:
        return "Odd"
    else:
        return "Even"

def main():
    n = int(input())
    ans = get_answer(n)
    print(ans)

def test():
    in1 = 3
    expect1 = "Odd"
    assert get_answer(in1) == expect1

    in2 = 1000
    expect2 = "Even"
    assert get_answer(in2) == expect2

test()
main()

# Q
# 論理積 (AND) 応用 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/bit_exhaustive_search/bit_exhaustive_search__bit_operation_step3
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 前回の問題で学習した論理積 (AND) をさらに使いこなせるようにしましょう。

# 整数 N の偶奇を、N と 1 の論理積をとることで判定してみましょう。
# N が偶数の場合は Even、奇数の場合は Odd を出力してください。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# N

# ・ 1 行目に整数 N が与えられます。
# ・ 入力は合計で 1 行からなり、入力値最終行の末尾に改行が 1 つ入ります。


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# N が偶数の場合はEven、奇数の場合はOddを出力してください。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 0 ≦ N ≦ 2^10

# 入力例1
# 3

# 出力例1
# Odd

# 入力例2
# 1000

# 出力例2
# Even