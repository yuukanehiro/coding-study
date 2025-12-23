
# ------------------------
# 素数を判定して返却
# ------------------------
def get_answer(n: int) -> str:
    if is_primer(n):
        return "YES"
    else:
        return "NO"

def is_primer(n: int):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    # 2以外の偶数はFalse
    if n % 2 == 0:
        return False

    # 2以外は偶数の素数は存在しない。
    # √nの範囲 and 奇数のみを効率よく探索    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

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
    in2 =  837
    assert get_answer(in2) == answer2

if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 素数判定 Python3編（paizaランク D 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__is_prime_easy
# 問題文のURLをコピーする
#  チャレンジする言語
# Python3
# 他の言語でチャレンジする
# コードを書いて解いてみる
# 問題
#  下記の問題をプログラミングしてみよう！
# 整数 N が与えられるので、N が素数かどうかを判定してください。
# なお、「整数 N が素数である」とは「N が 1 でない、かつ N の約数が 1 と N のみしか存在しない」ことをいいます。

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