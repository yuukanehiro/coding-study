

# 基本選択法 選択ソート
def get_asnwer(a: list[int]) -> list[int]:
    n = len(a)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]
    
    return a

def test():
    a = [9, 4, 7, 3, 1, 8, 5, 6, 2]
    expect = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert get_asnwer(a) == expect

test()