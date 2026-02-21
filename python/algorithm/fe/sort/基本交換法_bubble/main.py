



# 基本交換法_バブルソート
def get_answer(a: list[int]) -> list[int]:
    n = len(a)

    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

def test():
    in_a1 = [5, 1, 3, 4, 2]
    expect1 = [1, 2, 3, 4, 5]
    assert get_answer(in_a1) == expect1

test()

