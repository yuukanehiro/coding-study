from typing import List

# ------------------------
# を返却
# ------------------------
def get_answer(a: List[int], t: int) -> int:
    n = len(a)

    INF = 10**9
    dp = [INF] * (t + 1)
    
    # 0グラムの時はおもりは0個が最小
    dp[0] = 0

    for val in a:
        for j in range(t, val - 1, -1):
              dp[j] = min(dp[j], dp[j - val] + 1)

    if dp[t] != INF:
        return dp[t]
    else:
        return -1


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
    answer1 = 2
    a = [
        7,
        3,
        4,
        3,
        2,
    ]
    t = 10
    assert get_answer(a, t) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 部分和問題 3 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_partial_sums_step2
# 問題文のURLをコピーする
#  チャレンジする言語
# Python3
# 他の言語でチャレンジする
# コードを書いて解いてみる
# 問題
#  下記の問題をプログラミングしてみよう！
# 1 ~ n の番号がついた n 個のおもりがあり、おもり i の重さは a_i です。

# おもりを何個か選んで重さの和が x となるようにする方法を考えたとき、選ぶおもりの個数の最小値を出力してください。なお、同じおもりを2個以上選ぶことはできません。

# なお、重さの和が x となるようにおもりを選ぶ方法が存在しない場合は-1と出力してください。

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
# おもりを何個か選んで重さの和が x となるようにする方法のうち、選ぶおもりの個数の最小値を出力してください。

# ただし、重さの和が x となるようにおもりを選ぶ方法が存在しない場合は-1と出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 100

# ・ 1 ≦ x ≦ 1,000

# ・ 1 ≦ a_i ≦ 100

# 入力例1
# 5 10
# 7
# 3
# 4
# 3
# 2

# 出力例1
# 2
