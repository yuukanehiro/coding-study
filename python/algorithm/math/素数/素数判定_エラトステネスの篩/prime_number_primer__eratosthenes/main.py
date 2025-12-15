
# ------------------------
# エラトステネスの篩を利用して素数を返却
# refs: https://www.youtube.com/watch?v=CTgxfbXwKWY
# ------------------------
def get_answer(n: int) -> str:
    # 1. Trueで初期化
    is_primer = [True] * (n + 1)

    # 0, 1は素数ではない
    is_primer[0] = False
    is_primer[1] = False

    for i in range(2, n + 1):
        if is_primer[i]:
            for j in range(i * 2, n + 1, i):
                is_primer[j] = False

    if is_primer[n]:
        return "YES"
    else:
        return "NO"


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
    answer1 = "YES"
    in1 = 2
    assert get_answer(in1) == answer1

    answer2 = "NO"
    in2 = 837
    assert get_answer(in2) == answer2

if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# エラトステネスの篩 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__eratosthenes
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 整数 N が素数であるかを判定する方法として、エラトステネスの篩という方法があります。
# これは 0 以上 N 以下の全ての数について次の手順で素数判定を行う方法です。


# 1. X が素数のとき is_prime[X] が true となる配列 is_prime を用意し、
#     is_prime[0] , is_prime[1] を false , それ以外を true で初期化する。

# 2. 整数 i を 2 から順に N まで動かしながら次の操作を行う。
# 「is_prime[i] が true である場合、 is_prime[2×i], is_prime[3×i], ... , is_prime[k×i] を全て false にする（ただし k×i <= N ）


# 整数 N が与えられるので、エラトステネスの篩を用いて N が素数かどうかを判定してください。
# なお、「整数 N が素数である」とは「N が 1 でない、かつ N の約数が 1 と N のみしか存在しない」ことをいいます。
# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# N


# ・ 1 行で整数 N が与えられます。

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# N が素数である場合には "YES" を、素数でない場合は "NO" を 1 行で出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ・ 1 ≦ N ≦ 1,000,000

# 入力例1
# 2

# 出力例1
# YES

# 入力例2
# 837

# 出力例2
# NO