
def get_answer(n: int, a: int, b: int) -> int:
    # 最小値を求めたいので非常に大きい数を入れておく
    dp = [10000000] * (n + 1)

    dp[0] = 0

    # 1個の時はa
    dp[1] = a

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + a, dp[i - 2] + b)

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

    n, a, b = map(int, input().split())

    print(get_answer(n, a, b))

if __name__ == '__main__':
    main()

    answer1 = 400
    assert get_answer(5, 100, 150) == answer1



# Q
# 最安値を達成するには 1 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step0
# 問題文のURLをコピーする
#  チャレンジする言語
# Python3
# 他の言語でチャレンジする
# コードを書いて解いてみる
# 問題
#  下記の問題をプログラミングしてみよう！
# 八百屋にて、りんご1個が a 円で、りんご2個が b 円で売られています。

# りんごの買い方を工夫したとき、n 個のりんごを手に入れるために必要な金額の最小値はいくらでしょうか。なお、買い方を工夫した結果、買ったりんごが n+1 個以上になってもよいものとします。

# (ヒント)
# りんご1つあたりの値段を計算し、安いほうのりんごを買うことで金額の最小値を達成することもできますが、練習だと思ってDPで解いてみましょう。

# 部分問題として、りんご i 個 (1 ≦ i ≦ n-1) を買うのに必要な金額の最小値を求める問題を考えてみましょう。これらの問題の答えがすべて分かっているとして、n 個のりんごを買うのに必要な金額の最小値はどうなるかを考えてみましょう。少し考えると、n 個のりんごを最も安く買う方法は、

# n-1 個のりんごを最も安く買ってから最後に1個のりんごを a 円で買う
# n-2 個のりんごを最も安く買ってから最後に2個のりんごを b 円で買う
# の2通りのうち安いほうであることがわかります。なお、a < b という制約があるため、n-1 個のりんごを最も安く買ってから最後に1個買う代わりに2個買うのは常に無駄であることに注意しましょう。これで、部分問題と元の問題との関係が明らかになりました。dp[n] をちょうど n 個のりんごを買うのに必要な金額の最小値として、漸化式を立ててみましょう。(次セクションに答え)

# 漸化式を自力で立てられましたか？漸化式は dp[n] = min(dp[n-1] + a, dp[n-2] + b) となります。以下の疑似コードに従って、あなたの得意な言語で実装してみましょう。

# dp[0] <- 0
# dp[1] <- a

# for i = 2 to n
#     dp[i] <- min(dp[i-1] + a, dp[i-2] + b)

# print dp[n]
# 入力される値
# n a b

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# りんごを n 個手に入れるために必要な金額の最小値を出力してください。

# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≦ n ≦ 1,000

# ・ 1 ≦ a ≦ 10,000

# ・ 1 ≦ b ≦ 10,000

# ・ a < b

# 入力例1
# 5 100 150

# 出力例1
# 400
