from typing import List

# ------------------------
# を返却
# ------------------------
def get_answer(a: List[int], t: int) -> str:
    n = len(a)
    dp = [0] * (t + 1)

    # 0グラム指定の時はtrue
    dp[0] = 1

    for val in a:
        for j in range(t, val - 1, -1):
            if dp[j - val] == 1:
                dp[j] = 1

    if dp[t] == 1:
        return "yes"
    else:
        return "no"


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

    n, t = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    print(get_answer(a, t))


# ------------------------
# テストコード
# ------------------------
def test():
    answer1 = 'yes'
    a1 = [
        7,
        18,
        5,
        4,
        8,
    ]
    t1 = 19
    assert get_answer(a1, t1) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 部分和問題 1 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_partial_sums_step0
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 1 ~ n の番号がついた n 個のおもりがあり、おもり i の重さは a_i です。
# おもりを何個か選んで重さの和が x となるようにすることができるかどうか判定してください。なお、同じおもりを2個以上選ぶことはできません。

# (ヒント)
# おもり 1 ~ n を用いて重さの和を x となるようにすることができるか、という問題を考えるために、部分問題としておもり 1 ~ n-1 を用いて重さの和を x となるようにすることができるか、という問題を考えてみましょう。

# n-1 までのおもりを用いて重さの和を x または x-a_n となるようにすることができれば、おもり 1 ~ n を用いて重さの和を x となるようにすることができることがわかります。よって、最初はおもり 1 のみを使えることにして問題を解き、次にその結果を利用しておもり 1 ~ 2 を使えることにして問題を解く、ということを n まで繰り返せば、元の問題が解けそうです。

# dp_k[x] を、おもり k までを用いて重さの和が x となるようにすることができるかどうかを表す真偽値とすると、上で考察した関係は漸化式で表すと dp_k[x] = (dp_{k-1}[x] or dp_{k-1}[x-a_k]) となります。

# dp_1, dp_2, ... と順に dp_n まで計算すれば問題の答えを求めることができます。dp_1 から dp_n のそれぞれに対応する n 本の1次元配列 (もしくはこれに相当する2次元配列) を使って実装してもよいのですが、dp_k[x] を求めるには dp_{k-1}[x] と dp_{k-1}[x-a_k] さえわかっていれば十分であることを踏まえると、ループの回し方を以下の様に工夫することで、これまでと同じように1本の1次元配列で解くことができます。

# for i = 0 to x
#     dp[i] <- false

# dp[0] <- true   // おもりを選ばなければ、重さの和を0とすることができる

# for i = 1 to n  // おもり i までのおもりを使って
#     for j = x down to a_i    // 重さの和を j とすることができるか？
#         if dp[j-a_i] is true then
#             dp[j] <- true   

# if dp[x] is true then
#     print "yes"
# else
#     print "no"
# j を x から a_i へ減らす方向にループを回していることに注意してください。逆に a_i から x へ 増やす方向にループを回すと正しい答えが求められない可能性があります。理由を考えてみましょう (ヒント: n = 1, a_1 = 5, x = 10 のとき、ループの回し方によって答えはどうなるか？)

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# n x
# a_1
# a_2
# ...
# a_n


# ・ 1行目に、おもりの個数 n と目標とする重さの和 x が半角スペース区切りで与えられます。

# ・ 続く n 行のうち i 行目では、おもり i の重さ a_i が与えられます。


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# おもりを何個か選んで重さの和が x となるようにすることができるなら yes と、できないなら no と出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 100

# ・ 1 ≦ x ≦ 1,000

# ・ 1 ≦ a_i ≦ 100

# 入力例1
# 5 19
# 7
# 18
# 5
# 4
# 8

# 出力例1
# yes