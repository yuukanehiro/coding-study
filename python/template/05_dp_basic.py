"""
動的計画法（DP）基礎テンプレート（重要）
中堅以上のSaaS系ベンチャーで頻出
"""

# ====== 基本パターン ======

# 1次元DP
# dp[i] = i番目までの最適解
n = 10
dp = [0] * (n + 1)

for i in range(n):
    # 遷移式
    dp[i + 1] = max(dp[i], dp[i] + arr[i])

# 2次元DP
# dp[i][j] = i番目、状態jの最適解
h, w = 10, 10
dp = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        # 遷移式
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])

# ====== 典型問題 ======

# 問題1: フィボナッチ数列
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 問題2: ナップサック問題（容量制限付き）
def knapsack(weights, values, capacity):
    """
    weights: 各アイテムの重さ
    values: 各アイテムの価値
    capacity: ナップサックの容量
    """
    n = len(weights)
    # dp[i][w] = i番目までで容量wの最大価値
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n):
        for w in range(capacity + 1):
            # i番目を選ばない
            dp[i + 1][w] = dp[i][w]

            # i番目を選ぶ
            if w >= weights[i]:
                dp[i + 1][w] = max(
                    dp[i + 1][w],
                    dp[i][w - weights[i]] + values[i]
                )

    return dp[n][capacity]

# メモリ最適化版（1次元配列）
def knapsack_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # 逆順に更新（上書きを防ぐ）
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# 問題3: 最長共通部分列（LCS）
def lcs(s1, s2):
    """2つの文字列の最長共通部分列の長さ"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[m][n]

# 問題4: 編集距離（レーベンシュタイン距離）
def edit_distance(s1, s2):
    """s1をs2に変換するための最小編集回数"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初期化
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = min(
                    dp[i][j] + 1,      # 置換
                    dp[i + 1][j] + 1,  # 挿入
                    dp[i][j + 1] + 1   # 削除
                )

    return dp[m][n]

# 問題5: コイン問題（最小枚数）
def coin_change(coins, amount):
    """金額amountを作る最小コイン枚数"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(amount + 1):
        for coin in coins:
            if i + coin <= amount:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# 問題6: コイン問題（組み合わせ数）
def coin_combinations(coins, amount):
    """金額amountを作る組み合わせ数"""
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# 問題7: 最大部分配列和（連続）
def max_subarray_sum(arr):
    """連続する部分配列の最大和"""
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])

    return max(dp)

# Kadaneのアルゴリズム（メモリ効率版）
def max_subarray_kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# 問題8: グリッド上の最小コスト経路
def min_path_sum(grid):
    """左上から右下までの最小コスト"""
    h, w = len(grid), len(grid[0])
    dp = [[float('inf')] * w for _ in range(h)]
    dp[0][0] = grid[0][0]

    for i in range(h):
        for j in range(w):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

    return dp[h-1][w-1]

# 問題9: 部分和問題
def subset_sum(arr, target):
    """配列の部分集合でtargetを作れるか"""
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        # 逆順に更新
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True

    return dp[target]

# ====== DPのデバッグ ======

def print_dp_table(dp):
    """DPテーブルを見やすく出力"""
    for row in dp:
        print(' '.join(f'{x:4}' for x in row))
