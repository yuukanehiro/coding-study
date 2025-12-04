

def get_answer(n: int, a: int, b: int, c: int) -> int:
    dp = [0] * (n + 1)

    # 0段の時は1通り
    dp[0] = 1

    for i in range(1, n + 1):
        if i >= a:
            dp[i] += dp[i - a]
        if i >= b:
            dp[i] += dp[i - b]
        if i >= c:
            dp[i] += dp[i - c]     

    return dp[n]


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

    n, a, b, c = map(int, input().split())

    print(get_answer(n, a, b, c))


answer1 = 17
assert get_answer(10, 2, 3, 4) == answer1


if __name__ == '__main__':
    main()

# Q
# 【階段の上り方】階段の上り方 3 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_boss
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 整数 n, a, b, c が与えられます。
# 階段を上るのに、1歩で a 段または b 段または c 段を上ることができるとき、n 段の階段を上る方法は何通りあるでしょうか。

# (ヒント)
# 上り方が2つから3つへ増えましたが、やることは同じです。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# n a b c

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# n 段の階段を上る方法の数を1行に出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 30

# ・ 1 ≦ a ≦ 7

# ・ 1 ≦ b ≦ 7

# ・ 1 ≦ c ≦ 7

# ・ a ≠ b

# ・ b ≠ c

# ・ c ≠ a

# 入力例1
# 10 2 3 4

# 出力例1
# 17