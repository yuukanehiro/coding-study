from collections import defaultdict
from typing import List, Dict, Tuple

# ------------------------
# を返却
# ------------------------
def get_answer(heights: List[int]) -> int:
    dp = [1] * len(heights)

    for i in range(1, len(heights)):
        if heights[i - 1] >= heights[i]:
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

    n = int(input())
    heights = [int(input()) for _ in range(n)]
    print(get_answer(heights))


# ------------------------
# テストコード
# ------------------------
def test():
    answer1 = 3
    input1 = [187, 192, 115, 108, 109]
    assert get_answer(input1) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 【連続列】最長減少連続部分列 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_continuous_boss
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# n 人が横一列に並んでいます。左から i 番目の人を人 i と呼ぶことにします。人 i の身長は a_i [cm]です。

# 人 l ,人 l+1, ... , 人 r からなる区間 [l, r] について、すべての l ≦ i < r に対して a_i ≧ a_{i+1} が成り立っているとき、区間 [l, r] は逆背の順であると呼ぶことにします。また、区間 [l, r] の長さを r-l+1 とします。

# 逆背の順であるような区間のうち、最長であるものの長さを出力してください。

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
# 逆背の順であるような区間のうち、最長であるものの長さを出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 200,000

# ・ 100 ≦ a_i ≦ 200

# 入力例1
# 5
# 187
# 192
# 115
# 108
# 109

# 出力例1
# 3