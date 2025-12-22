from typing import List
# ------------------------
# nを構成素数の積を返却
# 構成する素数が複数ある場合は積の大きい組み合わせを返却
# ゴールドバッハ予想
# 4 × 10^18 までは「全ての 3 よりも大きな偶数は 2 つの素数の和として表すことができる。」
# ------------------------
def get_answer(n: int) -> List[int]:
    if n < 4:
        return []


    is_primers: List[bool] = [True] * (n + 1)
    is_primers[0] = False
    is_primers[1] = False

    # 素数判定の格納
    # エウストテネスの篩
    for i in range(2, n + 1):
        if is_primers[i]:
            for j in range(i * 2, n + 1, i):
                is_primers[j] = False
                
    
    multi = -1
    ans = [-1, -1]

    for p in range(n + 1):
        if is_primers[p]:
            other_prime = n - p
            if is_primers[other_prime]:
                if p * other_prime > multi:
                    multi = p * other_prime
                    ans = [p, other_prime]

    return ans


def main():
    n = int(input())
    a = (get_answer(n))
    for i in a:
        print(i)


# ------------------------
# テストコード
# ------------------------
def test():
    # inにNとa1,a2,aNがある場合にNが含めてしまうミスが多いので気をつける
    in1 = 4
    answer1 = [
        2,
        2,
    ]
    assert get_answer(in1) == answer1

    in2 = 108
    answer2 = [
        47,
        61,
    ]
    assert get_answer(in2) == answer2

if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# ゴールドバッハ予想 Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__goldbach_conjecture
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 素数に関連した数学の有名な未解決問題としてゴールドバッハ予想があります。その内容は次の通りです。
# 「全ての 3 よりも大きな偶数は 2 つの素数の和として表すことができる。」
# 全ての 3 よりも大きな偶数に対応する 2 つの素数が存在するかどうかはコンピュータを持ってしても確かめることができませんが、ある程度の大きさの数までならコンピュータで対応する 2 つの素数を求めることができます。
# 実際に 4 × 10^18 まではゴールドバッハ予想が成立することは証明されています。
# そこで、10^5 以下の偶数 N が与えられるので、 N を 2 つの素数の和で表し、出力してください。
# ただし、答えが複数個ある場合は、それらのうち、積が最も大きくなるような 2 つの素数を出力してください。（答えは 1 通りになることが保証されます。）

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# N


# ・ 1 行で整数 N が与えられます。

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# 足して N となる 2 つの素数のうち、積が最大であるものを小さい素数から順に改行区切りで 2 行で出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ・ 4 ≦ N ≦ 100,000
# ・ N は偶数である

# 入力例1
# 4

# 出力例1
# 2
# 2

# 入力例2
# 108

# 出力例2
# 47
# 61