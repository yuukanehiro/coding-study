from collections import defaultdict
from typing import List, Dict, Tuple

# ------------------------
# を返却
# ------------------------
def get_answer(heights: List[int]) -> int:
    dp = [1] * (len(heights))

    for i in range(1, len(heights)):
        if heights[i - 1] <= heights[i]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1

    return max(dp)


def main():
    # item_count, query_count = map(int, input().split())
    # n = int(input()) # 1つのintの場合
    # inputList = list(map(int, input().split()))
    # item_count, query_count = inputList[0], inputList[1]
    # items = [input().strip() for _ in range(item_count)]

    # n回のList[int]
    # n = int(input().strip())
    # heights = [int(input().strip()) for _ in range(n)]

    # 2次元配列
    # items = [list(map(int, input().split())) for _ in range(item_count)]
    # 1 - indexed
    # items = [0] + [int(input().strip()) for _ in range(item_count)]
    # queries = [input().strip() for _ in range(query_count)]
    # queries: Dict[int, str] = {int(line.split()[0]): line.split()[1] for line in (input().strip() for _ in range(query_count))}
    # queries: List[Tuple[int, str]] = [(int(line.split()[0]), line.split()[1]) for line in (input().strip() for _ in range(query_count))]

    n = int(input().strip())
    heights = [int(input().strip()) for _ in range(n)]
    print(get_answer(heights))


# ------------------------
# テストコード
# ------------------------
def test():
    answer1 = 3
    input1 = [160, 178, 170, 190, 190]
    assert get_answer(input1) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 最長増加連続部分列 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_continuous_step0
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# n 人が横一列に並んでいます。左から i 番目の人を人 i と呼ぶことにします。人 i の身長は a_i [cm]です。
# 人 l ,人 l+1, ... , 人 r からなる区間 [l, r] について、すべての l ≦ i < r に対して a_i ≦ a_{i+1} が成り立っているとき、区間 [l, r] は背の順であると呼ぶことにします。また、区間 [l, r] の長さを r-l+1 とします。
# 背の順であるような区間のうち、最長であるものの長さを出力してください。

# (ヒント)
# 元の問題を解くために、部分問題としてどのような問題を考えればよいでしょうか。

# dp[n] を、人 n が右端となっているような背の順区間のうち、最長であるような区間の長さとしてみましょう。dp[1] ~ dp[k-1] が既に求まっているとして、dp[k] がどうなるかを考えてみましょう。dp[k-1] に注目すると、dp[k-1] は人 k-1 を右端とする背の順区間の長さですから、もし a_{k-1} ≦ a_k なら、その区間の右端に人 k をくっつけることで新しく長さ dp[k-1]+1 の背の順区間を作ることができ、この区間の長さは人 k を右端として持つ背の順区間のうち最長であることがわかります。逆に、もし a_{k-1} ＞ a_k なら、人 k が右端となるような背の順区間は人 k のみからなる長さ1の区間しか存在しないことがわかります。

# 以上の考察により、dp[k-1] と dp[k] の関係が明らかになりました。自信のある人は自分で漸化式を立ててみましょう。以下の疑似コードに従って、自分の得意な言語で実装してみましょう。

# dp[1] <- 1

# for i = 2 to n
#     if a[i-1] <= a[i] then
#         dp[i] <- dp[i-1]+1
#     else
#         dp[i] <- 1

# print max({dp[1], ... ,dp[n]})
# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# n
# a_1
# a_2
# ...
# a_n


# ・ 1行目に、横一列に並んでいる人の人数 n が与えられます。

# ・ 続く n 行のうち i 行目では、人 i の身長 a_i が与えられます。


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# 背の順であるような区間のうち、最長であるものの長さを出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 200,000

# ・ 100 ≦ a_i ≦ 200

# 入力例1
# 5
# 160
# 178
# 170
# 190
# 190

# 出力例1
# 3