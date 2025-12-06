"""
CSV入力処理テンプレート
"""

import csv
from io import StringIO

# ====== 基本的なCSV入力パターン ======

# パターン1: カンマ区切りの1行入力
def read_csv_line():
    """
    入力例: 1,2,3,4,5
    """
    # 整数のリスト
    arr = list(map(int, input().split(',')))

    # 文字列のリスト
    strs = input().split(',')

    return arr

# パターン2: 複数行のCSV（ヘッダーなし）
def read_csv_no_header():
    """
    入力例:
    3
    1,Alice,90
    2,Bob,85
    3,Charlie,95
    """
    n = int(input())
    data = []

    for _ in range(n):
        row = input().split(',')
        # IDを整数、名前を文字列、スコアを整数に変換
        id = int(row[0])
        name = row[1]
        score = int(row[2])
        data.append([id, name, score])

    return data

# パターン3: ヘッダー付きCSV
def read_csv_with_header():
    """
    入力例:
    id,name,score
    1,Alice,90
    2,Bob,85
    3,Charlie,95
    """
    header = input().split(',')

    data = []
    try:
        while True:
            row = input().split(',')
            data.append(row)
    except EOFError:
        pass

    return header, data

# パターン4: csvモジュールを使う（推奨）
def read_csv_module():
    """
    csvモジュールを使うと、ダブルクォートやエスケープを自動処理
    """
    import sys

    reader = csv.reader(sys.stdin)
    data = []

    for row in reader:
        data.append(row)

    return data

# ====== よくある処理パターン ======

# パターン5: CSVを辞書のリストに変換
def csv_to_dict_list():
    """
    入力例:
    name,age,city
    Alice,25,Tokyo
    Bob,30,Osaka

    出力: [{'name': 'Alice', 'age': '25', 'city': 'Tokyo'}, ...]
    """
    header = input().split(',')

    data = []
    try:
        while True:
            row = input().split(',')
            record = dict(zip(header, row))
            data.append(record)
    except EOFError:
        pass

    return data

# パターン6: 特定のカラムでフィルタリング
def filter_by_column():
    """
    入力例:
    3
    Alice,90,Math
    Bob,85,Science
    Charlie,95,Math

    Mathの科目だけ抽出
    """
    n = int(input())
    results = []

    for _ in range(n):
        name, score, subject = input().split(',')
        if subject == 'Math':
            results.append([name, int(score), subject])

    return results

# パターン7: カラムで集計
def aggregate_by_column():
    """
    入力例:
    5
    Alice,Math,90
    Bob,Math,85
    Alice,Science,88
    Bob,Science,92
    Charlie,Math,95

    生徒ごとの合計点を計算
    """
    from collections import defaultdict

    n = int(input())
    scores = defaultdict(int)

    for _ in range(n):
        name, subject, score = input().split(',')
        scores[name] += int(score)

    return dict(scores)

# パターン8: CSVのソート
def sort_csv_data():
    """
    入力例:
    3
    Alice,90
    Charlie,95
    Bob,85

    スコアの降順でソート
    """
    n = int(input())
    data = []

    for _ in range(n):
        name, score = input().split(',')
        data.append([name, int(score)])

    # スコアの降順でソート
    data.sort(key=lambda x: -x[1])

    return data

# ====== 実践的な例題 ======

# 例題1: 売上データの集計
def sales_aggregation():
    """
    入力:
    4
    2024-01-01,Apple,100
    2024-01-01,Orange,80
    2024-01-02,Apple,120
    2024-01-02,Orange,90

    商品ごとの合計売上を計算
    """
    from collections import defaultdict

    n = int(input())
    sales = defaultdict(int)

    for _ in range(n):
        date, product, amount = input().split(',')
        sales[product] += int(amount)

    # 売上順にソート
    sorted_sales = sorted(sales.items(), key=lambda x: -x[1])

    return sorted_sales

# 例題2: ユーザーのログイン履歴
def login_history():
    """
    入力:
    5
    Alice,2024-01-01,login
    Bob,2024-01-01,login
    Alice,2024-01-01,logout
    Charlie,2024-01-02,login
    Bob,2024-01-02,logout

    現在ログイン中のユーザーを返す
    """
    n = int(input())
    logged_in = set()

    for _ in range(n):
        user, date, action = input().split(',')
        if action == 'login':
            logged_in.add(user)
        elif action == 'logout':
            logged_in.discard(user)

    return sorted(logged_in)

# 例題3: テストスコアの統計
def test_statistics():
    """
    入力:
    4
    Alice,90,85,88
    Bob,75,80,82
    Charlie,95,92,98
    David,60,65,70

    各生徒の平均点と最高点・最低点を計算
    """
    n = int(input())
    results = []

    for _ in range(n):
        row = input().split(',')
        name = row[0]
        scores = list(map(int, row[1:]))

        avg = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)

        results.append({
            'name': name,
            'average': avg,
            'max': max_score,
            'min': min_score
        })

    return results

# ====== CSVの出力 ======

# 出力パターン1: カンマ区切りで1行出力
def output_csv_line(arr):
    """配列をCSV形式で出力"""
    print(','.join(map(str, arr)))

# 出力パターン2: 複数行のCSV出力
def output_csv_rows(data):
    """2次元配列をCSV形式で出力"""
    for row in data:
        print(','.join(map(str, row)))

# 出力パターン3: csvモジュールで出力
def output_csv_module(data):
    """csvモジュールで出力（ダブルクォート対応）"""
    import sys
    writer = csv.writer(sys.stdout)
    writer.writerows(data)

# ====== エッジケース対策 ======

# 注意1: 空白を含むCSV
def csv_with_spaces():
    """
    入力: Alice, 90, Tokyo
    ↑カンマの後にスペースがある場合
    """
    row = input().split(',')
    # strip()で前後の空白を削除
    row = [x.strip() for x in row]
    return row

# 注意2: ダブルクォートで囲まれたCSV
def csv_with_quotes():
    """
    入力: "Alice","Tokyo, Japan",90
    ↑カンマを含む値がダブルクォートで囲まれている
    """
    import csv
    from io import StringIO

    line = input()
    reader = csv.reader(StringIO(line))
    row = next(reader)
    return row

# 注意3: 空のフィールド
def csv_with_empty_fields():
    """
    入力: Alice,,90
    ↑途中のフィールドが空
    """
    row = input().split(',')
    # 空文字列をNoneに変換
    row = [x if x else None for x in row]
    return row

# ====== 実践問題例 ======

def example_problem():
    """
    問題: 社員データから部署ごとの平均年齢を計算

    入力:
    5
    Alice,25,Engineering
    Bob,30,Engineering
    Charlie,28,Sales
    David,35,Sales
    Eve,22,Marketing

    出力:
    Engineering,27.5
    Marketing,22.0
    Sales,31.5
    """
    from collections import defaultdict

    n = int(input())
    dept_ages = defaultdict(list)

    for _ in range(n):
        name, age, dept = input().split(',')
        dept_ages[dept].append(int(age))

    # 部署ごとの平均年齢を計算
    results = []
    for dept in sorted(dept_ages.keys()):
        avg_age = sum(dept_ages[dept]) / len(dept_ages[dept])
        results.append([dept, avg_age])

    # 出力
    for dept, avg in results:
        print(f"{dept},{avg}")

# ====== まとめ ======

"""
CSV入力のポイント:

1. 基本は split(',') で十分
2. 空白やダブルクォートがある場合は csv モジュール
3. 集計は defaultdict が便利
4. フィルタリングはリスト内包表記
5. ソートは lambda を活用

よくある出題パターン:
- 売上データの集計
- ユーザー行動ログの分析
- テストスコアの統計
- 社員データの集計
- 在庫管理システム
"""

if __name__ == "__main__":
    # テスト用
    pass
