"""
二分探索テンプレート（最優先）
SaaS系ベンチャーで頻出
"""

import bisect

# ====== bisectモジュール（推奨） ======

# ソート済み配列arrに対して
arr = [1, 3, 5, 7, 9]

# x以上の最小要素のインデックス
idx = bisect.bisect_left(arr, x)

# xより大きい最小要素のインデックス
idx = bisect.bisect_right(arr, x)

# 要素を挿入（ソートを保ったまま）
bisect.insort(arr, x)

# ====== 手動実装（理解用） ======

def binary_search_leftmost(arr, target):
    """target以上の最小要素のインデックスを返す"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_rightmost(arr, target):
    """targetより大きい最小要素のインデックスを返す"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_exists(arr, target):
    """targetが存在するか判定"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# ====== 二分探索の応用 ======

# パターン1: 答えで二分探索
def is_valid(mid):
    """midが条件を満たすか判定"""
    # 問題に応じた判定処理
    pass

def binary_search_answer(left, right):
    """条件を満たす最小値/最大値を求める"""
    # 最小値を求める場合
    while left < right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    return left

# パターン2: 浮動小数点数の二分探索
def binary_search_float(left, right, epsilon=1e-9):
    """浮動小数点数で二分探索"""
    while right - left > epsilon:
        mid = (left + right) / 2
        if is_valid(mid):
            right = mid
        else:
            left = mid
    return left

# ====== よくある問題例 ======

# 例1: ソート済み配列でtarget以上の要素数
def count_greater_equal(arr, target):
    idx = bisect.bisect_left(arr, target)
    return len(arr) - idx

# 例2: 区間[a, b]に含まれる要素数
def count_in_range(arr, a, b):
    left = bisect.bisect_left(arr, a)
    right = bisect.bisect_right(arr, b)
    return right - left

# 例3: 最長増加部分列（LIS）の長さ
def lis_length(arr):
    from bisect import bisect_left
    dp = []
    for x in arr:
        idx = bisect_left(dp, x)
        if idx == len(dp):
            dp.append(x)
        else:
            dp[idx] = x
    return len(dp)
