from collections import defaultdict
from typing import List, Dict, Tuple

# ------------------------
# を返却
# ------------------------
def get_answer(n: int, x: int, a: int, y:int, b: int) -> int:
    dp = [10000000000000] * (n + y)

    # 0個の時は0円
    dp[0] = 0

    for i in range(1, n + y):
        if i >= x:
            dp[i] = min(dp[i], dp[i - x] + a)
        if i >= y:
            dp[i] = min(dp[i], dp[i - y] + b)

    # n個以上すべてで最小の料金
    return min(dp[n:])


def main():
    # item_count, query_count = map(int, input().split())
    # n = int(input()) # 1つのintの場合
    # inputList = list(map(int, input().split()))
    # item_count, query_count = inputList[0], inputList[1]
    # items = [input().strip() for _ in range(item_count)]
    # 2次元配列
    # items = [list(map(int, input().split())) for _ in range(item_count)]
    # 1 - indexed
    # items = [0] + [int(input().strip()) for _ in range(item_count)]
    # queries = [input().strip() for _ in range(query_count)]
    # queries: Dict[int, str] = {int(line.split()[0]): line.split()[1] for line in (input().strip() for _ in range(query_count))}
    # queries: List[Tuple[int, str]] = [(int(line.split()[0]), line.split()[1]) for line in (input().strip() for _ in range(query_count))]

    n, x, a, y, b = map(int, input().split())
    print(get_answer(n, x, a, y, b))


# ------------------------
# テストコード
# ------------------------
def test():
    answer1 = 200
    assert get_answer(4, 2, 110, 5, 200) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 最安値を達成するには 3 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step2
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 八百屋にて、りんご x 個が a 円で、りんご y 個が b 円で売られています。

# りんごの買い方を工夫したとき、最終的に n 個のりんごを手に入れるために必要な金額の最小値はいくらでしょうか。なお、買い方を工夫した結果、買ったりんごが n+1 個以上になってもよいものとします。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# n x a y b

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# りんごを n 個手に入れるために必要な金額の最小値を出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 1,000

# ・ 1 ≦ x ≦ 1,000

# ・ 1 ≦ y ≦ 1,000

# ・ x < y

# ・ 1 ≦ a ≦ 10,000

# ・ 1 ≦ b ≦ 10,000

# ・ a < b

# 入力例1
# 4 2 110 5 200

# 出力例1
# 200