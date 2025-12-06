"""
基本的な入力処理テンプレート
"""

# 1行の整数
n = int(input())

# 1行の複数整数（スペース区切り）
a, b, c = map(int, input().split())

# 複数行の整数をリストに格納
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 1行の複数整数をリストに格納
arr = list(map(int, input().split()))

# 複数行の複数整数を2次元リストに格納
h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

# 文字列のリスト
n = int(input())
strings = [input() for _ in range(n)]

# 文字列を1文字ずつリストに
s = list(input())

# 複数行の異なる型の入力
n = int(input())
for _ in range(n):
    name, age = input().split()
    age = int(age)
    # 処理

# 標準出力
print(answer)
print(*arr)  # リストをスペース区切りで出力
print('\n'.join(map(str, arr)))  # リストを改行区切りで出力
