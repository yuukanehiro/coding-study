

def get_answer(a: int, b: int, xs: list[int], qs: list[int]) -> tuple[list[str], list[list[int]]]:
    table = [[] for _ in range(100)]

    for x in xs:
        hash = (a * x + b) % 100
        table[hash].append(x)

    ans: list[str] = []
    for x in qs:
        hash = (a * x + b) % 100
        if x in table[hash]:
            ans.append("Yes")
        else:
            ans.append("No")

    return ans, table
    

def main():
    a, b = map(int, input().split())
    n = int(input())

    xs: list[int] = []
    qs: list[int] = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        if tmp[0] == 1:
            xs.append(tmp[1])
        elif tmp[0] == 2:
            qs.append(tmp[1])
        else:
            exit("panic")

    ans, table = get_answer(a, b, xs, qs)
    for i in ans:
        print(i)

    for t in table:
        print(" ".join(map(str, t)))


def test():
    in_a1 = 17
    in_b1 = 13
    in_xs1 = [
        1,
        2,
        3,
        4,
        5,
    ]
    in_qs1 = [
        4,
        7,
        2,
        1,
        6,
    ]
    expect1 = [
        "Yes",
        "No",
        "Yes",
        "Yes",
        "No"
    ]
    ans1, _ = get_answer(in_a1, in_b1, in_xs1, in_qs1)
    assert ans1 == expect1

main()
test()

# Q
# ハッシュテーブルを使おう Python3編（paizaランク C 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/hash_problems/hash_problems__hashtable_boss
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# ハッシュテーブル (チェイン法) を作り、データ (整数値) の挿入クエリと検索クエリを処理してください。

# ハッシュテーブルは要素数 100 の配列とし、配列の各要素にはデータのリストを格納することとします。なお、各要素の初期値は空リストとします。各リストには複数のデータが含まれる可能性がありますが、格納された順番にデータが並ぶように実装してください。

# ハッシュ関数は、入力で与えられる整数 a, b を用いて H(x) = (a * x + b) % 100 とします。

# クエリは、以下の形式で入力されます。


# 1 x
# ハッシュテーブルにデータ x を格納してください。

# 2 x
# ハッシュテーブルにデータ x が格納されているかどうかを調べてください。格納されているなら Yes と、格納されていないなら No と出力してください。


# すべてのクエリを処理したあと、ハッシュテーブルの状態を出力してください。
# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# a b
# q
# k_1
# k_2
# ...
# k_q


# k_i は、以下のいずれかの形式
# 1 x_i

# 2 x_i

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# クエリに従って出力をおこなってください。
# 全クエリを処理した後、ハッシュテーブルの状態を 100 行で出力してください。i 行目には、ハッシュテーブルの添字 i の位置に格納されているリストに含まれているデータを、格納された順に半角スペース区切りで出力してください。リストが空の場合は空行を出力してください。
# また、末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 入力はすべて整数
# ・ 1 ≦ a, b ≦ 1,000
# ・ a % 100 ≠ 0
# ・ 1 ≦ q ≦ 10,000
# ・ 0 ≦ x_i ≦ 1,000,000 (1 ≦ i ≦ q)
# ・ 同じ値が複数回格納されることはない

# 入力例1
# 17 13
# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 2 4
# 2 7
# 2 2
# 2 1
# 2 6

# 出力例1
# Yes
# No
# Yes
# Yes
# No






























# 1
















# 2
















# 3
















# 4
















# 5
