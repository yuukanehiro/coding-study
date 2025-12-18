from collections import defaultdict

# ------------------------
# 約数の合計を返却
# 整数 N をN = (p^n)(q^m)(r^l)... と素因数分解できるとき、約数の個数は(n+1)(m+1)(l+1)...となります。
# ------------------------
def get_answer(n: int) -> int:
    primers = defaultdict(int)

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            primers[i] += 1

            n //= i

    if n > 1:
        primers[n] += 1

    # 掛け算なので初期値1
    res = 1
    for k, v in primers.items():
        res *= v + 1

    return res



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
    print(get_answer(n))


# ------------------------
# テストコード
# ------------------------
def test():
    in1 = 15
    answer1 = 4
    assert get_answer(in1) == answer1

    in2 = 100
    answer2 = 9
    assert get_answer(in2) == answer2

if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 約数の個数 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__number_of_divisor
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 整数 N が与えられるので、N の約数が何個あるかを求めましょう。
# なお、ある整数 N の約数の個数は、N を素因数分解したときに現れる全ての{素数の累乗 + 1} の積であることが知られています。
# よって、整数 N をN = (p^n)(q^m)(r^l)... と素因数分解できるとき、約数の個数は(n+1)(m+1)(l+1)...となります。
# 例として、12 の約数の個数は 12 = 2^2 × 3^1 より、(2+1)×(1+1) = 6 個と求まります。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# N


# ・ 1 行で整数 N が与えられます。

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# N の約数の個数を 1 行で出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ・ 1 ≦ N ≦ 100,000

# 入力例1
# 15

# 出力例1
# 4

# 入力例2
# 100

# 出力例2
# 9