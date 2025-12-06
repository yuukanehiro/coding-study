

def get_answer(n: int, a: int, b: int) -> int:
    # 最小値を求めたいので非常に大きい数を入れておく
    dp = [10000000] * (n + 5)

    # 0個の時は0円
    dp[0] = 0

    # 1個の時は0円
    dp[1] = 10000000

    # 2個の時はa円
    dp[2] = a

    # 3個の時は買えない
    dp[3] = 10000000

    # 4個の時
    dp[4] = dp[2] + a

    # 5の時
    dp[5] = min(b, dp[4] + b)

    for i in range(6, n + 5):
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + a)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + b)

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

    n, a, b = map(int, input().split())

    print(get_answer(n, a, b))


# ------------------------
# テストコード
# ------------------------
def test():
    answer1 = 200
    assert get_answer(4, 110, 200) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 最安値を達成するには 2 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step1
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 八百屋にて、りんご2個が a 円で、りんご5個が b 円で売られています。
# りんごの買い方を工夫したとき、n 個のりんごを手に入れるために必要な金額の最小値はいくらでしょうか。なお、買い方を工夫した結果、買ったりんごが n+1 個以上になってもよいものとします。

# (ヒント)
# 前問の八百屋ではりんごが1個と2個で売られていましたが、本問の八百屋では2個と5個で売られています。この変更により、前問と同じようにして解こうとするとうまくいかなくなりました。理由を考えてみてください。

# 前問と同じように dp[n] をちょうど n 個のりんごを買うのに必要な金額の最小値とすると、dp[3] の値が正しく計算されないことがわかります。これは、りんごは2個ずつか5個ずつでしか買うことが出来ないため、3個のりんごをちょうど買う方法が存在しないからです。では、どうしたら dp[3] のような、2と5の組合せでは作れないような個数について最安値を計算することが出来るでしょうか。

# 問題文の最後の文に注目すると、買うりんごの数が3個以上になってもよいことがわかるので、ここで dp2[n] を n 個以上のりんごを買うのに必要な金額の最小値としてみましょう。dp と dp2 の定義から、dp2[n] = min(dp[n], dp[n+1], ...) であることがわかります。dp2[n] が求めたい答えになっています。

# dp は dp[n] までではなく、余裕をもって dp[n+4] 程度まで計算しておく必要があることに注意しましょう (実はこの問題においては dp[n+2] まで計算しておけば十分なのですが、ある程度多めに計算しておくと安心です) 。また、実は新しく dp2 という配列を用意せずとも、dp をうまく書き換えることで答えを求めることもできます。余裕があれば考えてみてください (ヒント:ループを回す順番を工夫) 。

# ▼　下記解答欄にコードを記入してみよう

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
# 4 110 200

# 出力例1
# 200