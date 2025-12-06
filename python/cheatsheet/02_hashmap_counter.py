"""
ハッシュマップ/辞書/カウンタテンプレート（最優先）
データ集計・カウント問題で必須
"""

from collections import defaultdict, Counter

# ====== 基本的な辞書操作 ======

# 初期化
d = {}
d = defaultdict(int)  # 存在しないキーは0
d = defaultdict(list)  # 存在しないキーは空リスト
d = defaultdict(set)  # 存在しないキーは空セット

# 要素の追加・更新
d[key] = value
d[key] += 1  # カウントアップ

# 要素の取得
value = d.get(key, default_value)  # キーがない場合はdefault_value
if key in d:
    value = d[key]

# 削除
del d[key]
d.pop(key, None)  # キーがなくてもエラーにならない

# ====== Counterの使い方 ======

# 文字列や配列の要素をカウント
arr = [1, 2, 2, 3, 3, 3]
counter = Counter(arr)
# Counter({3: 3, 2: 2, 1: 1})

# 最頻値
most_common = counter.most_common(1)  # [(3, 3)]
most_frequent_element = most_common[0][0]  # 3

# 全要素数
total = sum(counter.values())

# ====== よくある問題パターン ======

# パターン1: 出現回数をカウント
count = defaultdict(int)
for x in arr:
    count[x] += 1

# パターン2: グループ化（同じ値をまとめる）
groups = defaultdict(list)
for i, x in enumerate(arr):
    groups[x].append(i)

# パターン3: 2つの配列の対応関係
mapping = {}
for a, b in zip(arr1, arr2):
    mapping[a] = b

# パターン4: アナグラム判定
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

# パターン5: 2数の和がターゲットになるペアを探す
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# パターン6: 重複を除く
unique = set(arr)
unique_list = list(set(arr))

# パターン7: 辞書のソート
# キーでソート
sorted_by_key = sorted(d.items())
# 値でソート
sorted_by_value = sorted(d.items(), key=lambda x: x[1])
# 値で降順ソート
sorted_by_value_desc = sorted(d.items(), key=lambda x: x[1], reverse=True)

# ====== セット操作 ======

# 和集合
s1 | s2
# 積集合
s1 & s2
# 差集合
s1 - s2
# 対称差
s1 ^ s2
