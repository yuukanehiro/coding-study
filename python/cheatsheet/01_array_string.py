"""
配列・文字列操作テンプレート（最優先）
SaaS系ベンチャーで最も頻出
"""

# ====== 配列操作 ======

# ソート
arr.sort()  # 昇順
arr.sort(reverse=True)  # 降順

# カスタムソート（2次元配列）
# 例: [[3, 1], [1, 2], [2, 3]] を第2要素でソート
arr.sort(key=lambda x: x[1])

# 複数キーでソート（第1要素昇順、第2要素降順）
arr.sort(key=lambda x: (x[0], -x[1]))

# 最大値・最小値とそのインデックス
max_val = max(arr)
min_val = min(arr)
max_idx = arr.index(max(arr))

# 合計・平均
total = sum(arr)
avg = sum(arr) / len(arr)

# リスト内包表記
squares = [x**2 for x in arr]
evens = [x for x in arr if x % 2 == 0]

# スライス
arr[start:end]  # start以上end未満
arr[::-1]  # 反転
arr[::2]  # 2つおきに取得

# ====== 文字列操作 ======

# 文字列の分割・結合
words = s.split()  # スペースで分割
chars = list(s)  # 1文字ずつリストに
result = ''.join(chars)  # リストを結合

# 文字列の検索
s.find('abc')  # 最初の位置（見つからない場合-1）
s.count('a')  # 出現回数
'abc' in s  # 含まれているか

# 文字列の置換
s.replace('old', 'new')

# 大文字・小文字
s.upper()
s.lower()
s.swapcase()

# 文字の判定
c.isdigit()  # 数字か
c.isalpha()  # アルファベットか
c.islower()  # 小文字か
c.isupper()  # 大文字か

# ====== よくある問題パターン ======

# パターン1: 最大値の更新
max_val = float('-inf')
for x in arr:
    max_val = max(max_val, x)

# パターン2: 累積和
cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + arr[i]
# 区間[l, r)の合計: cumsum[r] - cumsum[l]

# パターン3: 尺取り法（2ポインタ）
left = 0
for right in range(n):
    # 条件を満たす間leftを進める
    while left < right and condition:
        left += 1

# パターン4: スライディングウィンドウ
from collections import deque
window = deque()
for i in range(n):
    window.append(arr[i])
    if len(window) > k:
        window.popleft()
