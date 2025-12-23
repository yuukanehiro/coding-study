from typing import List

def is_primer(n: int) -> bool:
    # 2未満はFalse
    if n < 2:
        return False
    # 2は素数
    if n == 2:
        return True
    # 2以外の偶数はFalse
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        
    return True

def get_answer() -> List[int]:
    ans = []

    # 2^2 から 10000^2 までをチェック
    for i in range(2, 10001):
        square_num = i * i

        # ゴールドバッハ予想により3以上の偶数は2つの素数の和で表現できる のでスキップ
        if square_num % 2 == 0:
            continue

        if not is_primer(square_num - 2):
            ans.append(square_num)

    return ans

def main():
    r = get_answer()

    if len(r) == 0:
        print("paiza's conjecture is correct.")

    for i in r:
        print(i)


main()

# Q
# paiza 予想 Python3編（paizaランク B 相当）
# 問題にチャレンジして、ユーザー同士で解答を教え合ったり、コードを公開してみよう！

# シェア用URL:
# https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__paiza_conjecture
# 問題文のURLをコピーする
#  下記の問題をプログラミングしてみよう！
# 今の時点でゴールドバッハ予想（「全ての 3 よりも大きな偶数は 2 つの素数の和として表すことができる。」）に反例がないことを知った paiza 君は、
# 自分もそれっぽい予想を言えば数学界に名を残せるのではないかと思い、正しいかもわからない次の paiza 予想を立てました。

# 「全ての 3 よりも大きな平方数は 2 つの素数の和として表すことができる。」

# この予想が正しいかどうかを検証するために、4 以上 10^8 以下の平方数（9999 個）の中に paiza 予想を満たさないものが存在するかを調べましょう。

# ▼　下記解答欄にコードを記入してみよう

# 入力される値
# ありません


# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。 標準入力からの値取得方法はこちらをご確認ください
# 期待する出力
# paiza 予想が正しい場合、1 行で "paiza's conjecture is correct." と出力してください。
# 正しくない場合、4 以上 10^8 以下の平方数のうち paiza 予想を満たさないものを小さい方から改行区切りで出力してください。
# 出力の末尾には改行を入れてください。

# 条件
# ありません