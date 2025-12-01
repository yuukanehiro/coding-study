"""
貪欲法（Greedy）テンプレート
その場その場で最良の選択をする
"""

# ====== 貪欲法の基本 ======

# 貪欲法が使える条件:
# 1. 局所最適解が全体最適解につながる
# 2. 選択を取り消す必要がない

# ====== 典型問題 ======

# 問題1: 区間スケジューリング
def interval_scheduling(intervals):
    """
    重ならない区間を最大数選ぶ
    intervals: [(start, end), ...]
    """
    # 終了時刻でソート
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        # 前の区間と重ならない
        if start >= last_end:
            count += 1
            last_end = end

    return count

# 問題2: 最小硬貨問題
def min_coins(amount, coins):
    """
    貪欲法で硬貨の最小枚数を求める
    注意: 硬貨の種類によっては最適解が得られない
    """
    coins.sort(reverse=True)  # 大きい順
    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count if amount == 0 else -1

# 問題3: 活動選択問題
def activity_selection(activities):
    """
    開始時刻と終了時刻が与えられた活動から
    最大数の活動を選ぶ
    """
    # 終了時刻でソート
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_end = activities[0][1]

    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_end:
            selected.append(activities[i])
            last_end = end

    return len(selected)

# 問題4: 最小の会議室数
def min_meeting_rooms(intervals):
    """
    すべての会議を行うのに必要な最小会議室数
    """
    starts = sorted([x[0] for x in intervals])
    ends = sorted([x[1] for x in intervals])

    rooms = 0
    max_rooms = 0
    i, j = 0, 0

    while i < len(starts):
        if starts[i] < ends[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            rooms -= 1
            j += 1

    return max_rooms

# 問題5: ジャンプゲーム
def can_jump(nums):
    """
    各要素は最大ジャンプ長
    最後まで到達できるか
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True

# 問題6: ガソリンスタンド
def can_complete_circuit(gas, cost):
    """
    循環ルートを完走できる開始地点を返す
    """
    total_gas = 0
    current_gas = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            start = i + 1
            current_gas = 0

    return start if total_gas >= 0 else -1

# ====== 貪欲法のパターン ======

# パターン1: 最大/最小を繰り返し選ぶ
def greedy_max_selection(arr, k):
    """最大k個の要素を選ぶ"""
    arr.sort(reverse=True)
    return sum(arr[:k])

# パターン2: 交換可能な選択
def greedy_swap(arr):
    """隣接要素を交換して最適化"""
    # 例: バブルソートのような交換
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# パターン3: イベントソート
def event_sort(events):
    """
    開始イベントと終了イベントに分けてソート
    """
    events_list = []

    for start, end in events:
        events_list.append((start, 1))   # 開始
        events_list.append((end, -1))    # 終了

    events_list.sort()

    current = 0
    max_overlap = 0

    for time, delta in events_list:
        current += delta
        max_overlap = max(max_overlap, current)

    return max_overlap

# ====== DPとの使い分け ======

# 貪欲法が使える: 硬貨の種類が [1, 5, 10, 50, 100, 500]
# DPが必要: 硬貨の種類が [1, 3, 4] など特殊な場合

def should_use_greedy(problem):
    """
    貪欲法を使うべきか判断
    - 局所最適 = 全体最適 なら貪欲法
    - そうでなければDP
    """
    pass
