
# ------------------------
# nが素数かどうかを返却
# ------------------------
def get_answer(n: int) -> str:
    primers = []

    for i in range(2, n + 1):
        if is_primer(i):
            # 素数として登録
            primers.append(i)

    # print(f"primers: {primers}")
    # Output:
    # primers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    if n in primers:
        return "YES"
    else:
        return "NO"

# ------------------------
# 素数判定
# ------------------------
def is_primer(n: int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, n):
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

    n = 57 # グロタンディーク素数
    print(get_answer(n))


# ------------------------
# テストコード
# ------------------------
def test():
    answer1 = "NO"
    in1 = 57
    assert get_answer(in1) == answer1


if __name__ == '__main__':
    # テスト
    test()

    # 本処理
    main()

# Q
# グロタンディーク素数 Python3編（paizaランク D 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__grothendieck
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# ドイツ出身の著名な数学者であるアレクサンドル・グロタンディークは、講演の際に素数の具体例として 57 を挙げたと言われています。
# この 57 という数字に深い意味はないので、きっとグロタンディークは感覚派な数学者だったのでしょう。
# このエピソードから、 57 という数字はグロタンディーク素数と呼ばれています。
# この 57 という数字が本当に素数であるかを判定してください。
# なお、「整数 N が素数である」とは「N が 2 以上で、かつ N の約数が 1 と N のみしか存在しない」ことをいいます。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# ありません


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# 57 が素数である場合には "YES" を、素数でない場合は "NO" を 1 行で出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ありません