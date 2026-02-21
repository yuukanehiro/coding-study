"""
ハッシュ探索（チェイン法）
衝突時は同じ位置にリストで連結して格納
"""


def hash_func(key: int, size: int) -> int:
    """ハッシュ関数: 剰余を使う"""
    return key % size


class HashTable:
    """チェイン法"""

    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key: int) -> int:
        """挿入し、格納位置を返す"""
        index = hash_func(key, self.size)
        self.table[index].append(key)
        return index

    def search(self, key: int) -> int:
        """探索し、位置を返す。なければ-1"""
        index = hash_func(key, self.size)

        if key in self.table[index]:
            return index

        return -1


def get_answer(keys: list, target: int, size: int) -> int:
    """keysを格納後、targetの位置を返す"""
    ht = HashTable(size)
    for key in keys:
        ht.insert(key)
    return ht.search(target)


def main():
    size = int(input())
    keys = list(map(int, input().split()))
    target = int(input())

    result = get_answer(keys, target, size)
    print(result)


def test():
    # テーブルサイズ10、キー[12, 25, 36, 42]を格納
    # 12 % 10 = 2, 25 % 10 = 5, 36 % 10 = 6, 42 % 10 = 2

    ht = HashTable(10)
    assert ht.insert(12) == 2
    assert ht.insert(25) == 5
    assert ht.insert(36) == 6
    assert ht.insert(42) == 2  # 衝突しても同じ位置

    # table[2] = [12, 42] となる
    assert ht.table[2] == [12, 42]

    assert ht.search(12) == 2
    assert ht.search(42) == 2  # 同じ位置
    assert ht.search(99) == -1


test()
main()
