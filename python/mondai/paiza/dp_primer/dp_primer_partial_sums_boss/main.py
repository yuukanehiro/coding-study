from typing import List

# ------------------------
# を返却
# ------------------------
def get_answer(a: List[int], t: int) -> str:
    dp = [0] * (t + 1)

    # 0段の時は1通り
    dp[0] = 1

    for val in a:
        # 「無限個使える」= unbounded knapsack（完全ナップサック）なので、ループは 正順（小→大）に回す必要があり
        # unbounded knapsack / 完全ナップサック DP
        for j in range(val, t + 1):
            if dp[j - val]:
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
    answer1 = "yes"
    a = [
        9,
        3,
        4,
        11,
        8,
    ]
    t = 10
    assert get_answer(a, t) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 【部分和】部分和問題 4 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_partial_sums_boss
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 1 ~ n の番号がついた n 種類のおもりがあり、おもり i の重さは a_i です。それぞれのおもりは無限個存在しており、任意のおもりを任意の個数使うことができます。

# このとき、おもりを選んで重さの和を x となるようにすることができるかどうか判定してください。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# n x
# a_1
# a_2
# ...
# a_n


# ・ 1行目に、おもりの種類数 n と目標とする重さの和 x が半角スペース区切りで与えられます。

# ・ 続く n 行のうち i 行目では、おもり i の重さ a_i が与えられます。


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# 重さの和が x となるようにおもりを選ぶことができるなら yes と、できないなら no と出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 100

# ・ 1 ≦ x ≦ 1,000

# ・ 1 ≦ a_i ≦ 100

# 入力例1
# 5 10
# 9
# 3
# 4
# 11
# 8

# 出力例1
# yes