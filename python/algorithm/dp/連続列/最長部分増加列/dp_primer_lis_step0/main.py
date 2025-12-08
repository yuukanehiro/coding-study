from collections import defaultdict
from typing import List, Dict, Tuple

# ------------------------
# を返却
# ------------------------
def get_answer(a: List[int]) -> int:
    n = len(a)
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if a[j] < a[i]:
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
    answer1 = 3
    a = [
        100,
        102,
        101,
        91,
        199,
    ]
    assert get_answer(a) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 最長部分増加列 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_step0
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# n 本の木が横一列に並んでいます。左から i 番目の木を木 i と呼ぶことにします。木 i の高さは a_i [cm] です。
# あなたは、何本かの木を伐採することによって、残った木を左から順に見ると高さが単調増加になっているようにしたいと考えています。つまり、残った木を左から 木 k_1, 木 k_2, ... , 木 k_m とすると、a_{k_1} < a_{k_2} < ... < a_{k_m} が満たされているようにしたいです。なるべく多くの木が残るように、伐採する木を工夫して選んだとき、伐採されずに残る木の本数が最大でいくつになるか求めてください。
# なお、最初から n 本の木が単調増加に並んでいる場合は、1本も伐採しなくてよいものとします。

# (ヒント)
# まずは問題を整理しましょう。この問題は、添字の部分列 x1 < x2 < ... < xk であって、a_x1 < a_x2 < ... < a_xk を満たしているようなもの (これを、一般に増加部分列と呼びます) のうち、k が最も大きいもの (これを、一般に最長増加部分列 (Longest Increasing Subsequence, LIS) と呼びます) を求めよという問題に言い換えることができます。

# dp[k] を、最後が木 k であるような増加部分列のうち最長であるものの長さとしてみましょう。dp[1] ~ dp[k-1] が求まっているとして、dp[k] とこれらの関係はどのようになっているかを考えてみましょう。

# 少し考えると、1以上 k 未満の i について a_i < a_k が成り立っているとき、最後が木 i であるような増加部分列の最後に木 k をくっつけることで、新しく長さ dp[i] + 1 の増加部分列を作れることがわかります。そして、最後が木 k であるような最長増加部分列は、このようにして作られる部分列のうち最長のものであることがわかります。

# これで、dp[1] ~ dp[k-1] と dp[k] の関係が明らかになりました。自信のある方は自分で漸化式を立ててみましょう。以下の疑似コードに従ってあなたの得意な言語で実装してみましょう。

# dp[1] <- 1

# for i = 2 to n
#     dp[i] <- 1  // 木 i のみからなる部分列の長さ
#     for j = 1 to i-1
#         if a[j] < a[i] then
#             dp[i] <- max(dp[i], dp[j]+1)    // 最後が木 j であるような増加部分列の末尾に木 i をくっつける

# print max({dp[1], ... ,dp[n]})
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
# 残った木を左から見ると高さが単調増加になっているように木を伐採したとき、伐採されずに残る木の本数の最大値を出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 5,000

# ・ 1 ≦ a_i ≦ 1,000,000,000

# ・ a_i ≠ a_j (i ≠ j)

# 入力例1
# 5
# 100
# 102
# 101
# 91
# 199

# 出力例1
# 3