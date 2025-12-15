from collections import defaultdict
from typing import List, Dict, Tuple

# ------------------------
# を返却
# ------------------------
def get_answer(n: int) -> str:
    if is_primer(n):
        return "YES"
    else:
        return "NO"


def is_primer(n: int) -> bool:
    # 素数の定義から、1は素数ではない
    if n <= 1:
        return False
    # 素数の定義から、2は素数
    if n == 2:
        return True
    
    # 素数の定義から、2以外の偶数は素数ではない
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        
        # 次の奇数へ
        i += 2
        
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
    answer1 = "NO"
    in1 = 15
    assert get_answer(in1) == answer1

    answer2 = "YES"
    in2 = 2147483647
    assert get_answer(in2) == answer2

if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 大きな数の素数判定 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__is_prime_normal
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 整数 N が与えられるので、N が素数かどうかを判定してください。
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
# ・ 1 ≦ N ≦ 1,000,000,000,000

# 入力例1
# 15

# 出力例1
# NO

# 入力例2
# 2147483647

# 出力例2
# YES