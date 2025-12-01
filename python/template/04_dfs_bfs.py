"""
DFS/BFSテンプレート（重要）
グラフ・木構造の探索で頻出
"""

from collections import deque, defaultdict

# ====== グラフの表現 ======

# 隣接リスト（推奨）
n = 5  # ノード数
graph = [[] for _ in range(n)]
# 辺の追加（無向グラフ）
graph[u].append(v)
graph[v].append(u)

# 辺の追加（有向グラフ）
graph[u].append(v)

# 重み付きグラフ
graph[u].append((v, weight))

# ====== DFS（深さ優先探索） ======

# 再帰版（推奨）
def dfs_recursive(node, visited, graph):
    visited[node] = True

    # 訪問時の処理
    print(node)

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs_recursive(next_node, visited, graph)

# 使用例
visited = [False] * n
dfs_recursive(0, visited, graph)

# スタック版（明示的）
def dfs_stack(start, graph):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for next_node in graph[node]:
            if next_node not in visited:
                stack.append(next_node)

# ====== BFS（幅優先探索） ======

def bfs(start, graph):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

# 最短距離を求めるBFS
def bfs_distance(start, graph, n):
    dist = [-1] * n
    dist[start] = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                queue.append(next_node)

    return dist

# ====== グリッド上の探索 ======

# 4方向
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 8方向
dx8 = [-1, -1, -1, 0, 0, 1, 1, 1]
dy8 = [-1, 0, 1, -1, 1, -1, 0, 1]

def grid_bfs(start_i, start_j, grid):
    h, w = len(grid), len(grid[0])
    visited = [[False] * w for _ in range(h)]
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            # 範囲チェック
            if 0 <= ni < h and 0 <= nj < w:
                # 障害物でなく、未訪問
                if not visited[ni][nj] and grid[ni][nj] != '#':
                    visited[ni][nj] = True
                    queue.append((ni, nj))

# グリッド上の最短距離
def grid_shortest_path(start, goal, grid):
    h, w = len(grid), len(grid[0])
    dist = [[-1] * w for _ in range(h)]
    si, sj = start
    gi, gj = goal

    dist[si][sj] = 0
    queue = deque([(si, sj)])

    while queue:
        i, j = queue.popleft()

        if (i, j) == (gi, gj):
            return dist[gi][gj]

        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            if 0 <= ni < h and 0 <= nj < w:
                if dist[ni][nj] == -1 and grid[ni][nj] != '#':
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))

    return -1  # 到達不可能

# ====== よくある問題パターン ======

# パターン1: 連結成分の数
def count_components(n, graph):
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            dfs_recursive(i, visited, graph)
            count += 1

    return count

# パターン2: 島の数（グリッド）
def count_islands(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False] * w for _ in range(h)]
    count = 0

    def dfs(i, j):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if visited[i][j] or grid[i][j] == 0:
            return

        visited[i][j] = True
        for k in range(4):
            dfs(i + dx[k], j + dy[k])

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count

# パターン3: サイクル検出（無向グラフ）
def has_cycle_undirected(n, graph):
    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True

        for next_node in graph[node]:
            if not visited[next_node]:
                if dfs(next_node, node):
                    return True
            elif next_node != parent:
                return True

        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False
