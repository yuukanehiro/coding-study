from collections import defaultdict
from typing import List, Dict, Tuple

# ------------------------
# を返却
# ------------------------
def get_answer(a: List[int]) -> List[str]:
    answer: List[str] = []

    if len(a) == 0:
        return []

    for i in a:
        if is_primer(i):
            answer.append("pass")
        else:
            answer.append("failure")
    
    return answer

def is_primer(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        
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
    arr = [int(input()) for _ in range(n)]
    for v in get_answer(arr):
        print(v)


# ------------------------
# テストコード
# ------------------------
def test():
    # test1
    answer1 = [
        "pass",
        "failure",
        "pass",
        "failure",
        "failure",
    ]
    arr1 = [
        5,
        6,
        7,
        8,
        9,
    ]
    assert get_answer(arr1) == answer1

    # test2
    answer2 = [
        "failure",
        "failure",
        "failure",
        "pass",
        "failure",
        "failure",
        "failure",
        "failure",
        "pass",
        "failure",
        "failure",
        "failure",
        "failure",
        "failure",
        "failure",
    ]
    arr2 = [
        1066,
        9116,
        4350,
        8707,
        99614,
        48979,
        51412,
        26894,
        11779,
        3082,
        96436,
        43526,
        45530,
        6694,
        71442,
    ]
    assert get_answer(arr2) == answer2


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# 素数大学 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__is_prime_multi
# 問題文のURLをコピーする
#  チャレンジする言語
# Python3
# 他の言語でチャレンジする
# コードを書いて解いてみる
# 問題
#  下記の問題をプログラミングしてみよう！
# 素数大学学長に就任した paiza 君は素数が好きすぎるあまり、受験番号が素数の生徒を全員合格、素数でない生徒を全員不合格とすることにしました。
# N 人の受験生の受験番号 A_1 , ... ,A_N が与えられるので、各受験生について合否を判定してください。
# なお、「整数 N が素数である」とは「N が 1 でない、かつ、N の約数が 1 と N のみしか存在しない」ことをいいます。

# 入力される値
# N
# A_1
# ...
# A_N


# ・ 1 行目で与えられる整数の個数 N が与えられます。
# ・ 続く N 行のうち i 行目では i 個目の整数 A_i が与えられます。(1 ≦ i ≦ N)

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# 合計 N 行出力してください。
# i 行目には、受験番号 A_i の生徒が合格の場合には "pass" を、不合格の場合には "failure" を出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ・ 1 ≦ N ≦ 380,000
# ・ 1 ≦ A_i ≦ 6,000,000 (1 ≦ i ≦ N)

# 入力例1
# 5
# 5
# 6
# 7
# 8
# 9

# 出力例1
# pass
# failure
# pass
# failure
# failure

# 入力例2
# 15
# 1066
# 9116
# 4350
# 8707
# 99614
# 48979
# 51412
# 26894
# 11779
# 3082
# 96436
# 43526
# 45530
# 6694
# 71442

# 出力例2
# failure
# failure
# failure
# pass
# failure
# failure
# failure
# failure
# pass
# failure
# failure
# failure
# failure
# failure
# failure