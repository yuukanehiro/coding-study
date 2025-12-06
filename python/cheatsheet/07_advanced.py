"""
応用アルゴリズム集
Union-Find、累積和、ヒープなど
"""

from collections import defaultdict
import heapq

# ====== Union-Find（素集合データ構造） ======

class UnionFind:
    """Union-Find (Disjoint Set Union)"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        """xの根を見つける（経路圧縮）"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """xとyを結合"""
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        # ランクによる最適化
        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True

    def same(self, x, y):
        """xとyが同じグループか"""
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """xのグループのサイズ"""
        return self.size[self.find(x)]

    def groups(self):
        """全グループを辞書で返す"""
        groups = defaultdict(list)
        for i in range(len(self.parent)):
            groups[self.find(i)].append(i)
        return dict(groups)

# 使用例
# uf = UnionFind(n)
# uf.union(a, b)
# if uf.same(a, b): ...

# ====== 累積和 ======

# 1次元累積和
def cumsum_1d(arr):
    """1次元累積和の構築"""
    n = len(arr)
    cumsum = [0] * (n + 1)
    for i in range(n):
        cumsum[i + 1] = cumsum[i] + arr[i]
    return cumsum

def range_sum(cumsum, l, r):
    """区間[l, r)の和"""
    return cumsum[r] - cumsum[l]

# 2次元累積和
def cumsum_2d(grid):
    """2次元累積和の構築"""
    h, w = len(grid), len(grid[0])
    cumsum = [[0] * (w + 1) for _ in range(h + 1)]

    for i in range(h):
        for j in range(w):
            cumsum[i+1][j+1] = (cumsum[i][j+1] +
                                cumsum[i+1][j] -
                                cumsum[i][j] +
                                grid[i][j])
    return cumsum

def range_sum_2d(cumsum, r1, c1, r2, c2):
    """
    2次元累積和で矩形領域の和を求める
    (r1, c1)から(r2, c2)まで（0-indexed、r2, c2含まない）
    """
    return (cumsum[r2][c2] -
            cumsum[r1][c2] -
            cumsum[r2][c1] +
            cumsum[r1][c1])

# いもす法（区間加算）
def imos_1d(n, ranges):
    """
    いもす法で区間加算を高速化
    ranges: [(l, r, val), ...] 区間[l, r)にvalを加算
    """
    imos = [0] * (n + 1)

    for l, r, val in ranges:
        imos[l] += val
        imos[r] -= val

    # 累積和を取る
    for i in range(n):
        imos[i + 1] += imos[i]

    return imos[:n]

# ====== 優先度付きキュー（ヒープ） ======

# 最小ヒープ
def heap_example():
    heap = []
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 7)

    min_val = heapq.heappop(heap)  # 3

# 最大ヒープ（値を反転）
def max_heap_example():
    heap = []
    heapq.heappush(heap, -5)
    heapq.heappush(heap, -3)
    heapq.heappush(heap, -7)

    max_val = -heapq.heappop(heap)  # 7

# K番目に小さい要素
def kth_smallest(arr, k):
    """K番目に小さい要素を求める"""
    heap = arr[:k]
    heapq.heapify(heap)

    for num in arr[k:]:
        if num < heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]

# ダイクストラ法（最短経路）
def dijkstra(graph, start, n):
    """
    ダイクストラ法で単一始点最短経路
    graph: {node: [(next_node, cost), ...]}
    """
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)

    while heap:
        d, node = heapq.heappop(heap)

        if d > dist[node]:
            continue

        for next_node, cost in graph[node]:
            new_dist = d + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist

# ====== 尺取り法（2ポインタ） ======

def two_pointers_sum(arr, target):
    """
    ソート済み配列で2数の和がtargetになるペア
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

def sliding_window(arr, k):
    """
    長さkのウィンドウの最大和
    """
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# ====== トポロジカルソート ======

def topological_sort(graph, n):
    """
    トポロジカルソート（有向非巡回グラフ）
    graph: {node: [next_nodes...]}
    """
    from collections import deque

    # 入次数を計算
    indegree = [0] * n
    for node in graph:
        for next_node in graph[node]:
            indegree[next_node] += 1

    # 入次数0のノードをキューに
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    # サイクルがある場合は空リスト
    return result if len(result) == n else []

# ====== ビット演算 ======

# ビット全探索
def bit_brute_force(n):
    """
    n個の要素の全部分集合を列挙
    """
    for mask in range(1 << n):  # 2^n通り
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(i)
        # subsetを使った処理

# ビット演算の基本
def bit_operations():
    # i番目のビットが立っているか
    is_set = (mask >> i) & 1

    # i番目のビットを立てる
    mask |= (1 << i)

    # i番目のビットを消す
    mask &= ~(1 << i)

    # i番目のビットを反転
    mask ^= (1 << i)

    # 立っているビットの数
    count = bin(mask).count('1')

    # 最下位の立っているビット
    lowest = mask & -mask

# ====== セグメント木（Segment Tree） ======

class SegmentTree:
    """セグメント木（区間最小値クエリ）"""

    def __init__(self, arr):
        n = len(arr)
        self.n = 1
        while self.n < n:
            self.n *= 2

        self.tree = [float('inf')] * (2 * self.n)
        for i in range(n):
            self.tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])

    def update(self, idx, val):
        """idx番目をvalに更新"""
        idx += self.n
        self.tree[idx] = val

        while idx > 1:
            idx //= 2
            self.tree[idx] = min(self.tree[2*idx], self.tree[2*idx+1])

    def query(self, l, r):
        """区間[l, r)の最小値"""
        l += self.n
        r += self.n
        res = float('inf')

        while l < r:
            if l & 1:
                res = min(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = min(res, self.tree[r])
            l //= 2
            r //= 2

        return res
