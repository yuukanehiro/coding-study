

# 基本挿入法 挿入ソート
def get_answer(a: list[int]) -> list[int]:
    n = len(a)

    for i in range(1, n):
        temporary = a[i]
        j = i - 1

        while j >=0 and a[j] > temporary:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = temporary
    
    return a


def test():
    in_a1 = [5, 4, 6, 3, 7, 8, 2, 1, 9]
    expect1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert get_answer(in_a1) == expect1

test()

# [2, 1, 3,4]
# 1回目
# i = 1
# j = 0 ... 初期値
# temporary = 1

# while 1回目
# while
#     data[j](v2) > temporary(v1)
#     data[j + 1] = data[j] // [2, 2, 3, 4]
#     j -= 1 (v-1)
# data[-1 + 1] = temporary // [1, 2, 3, 4]

# 2回目
# i = 2
# j = 1 ... 初期値
# temporary = 3
# while 1回目 j = 1
# while
#     data[j](v2) > temporary(v3)
#     // 変更なし
# data[1 + 1] = temporary // [1, 2, 3, 4] // 変更なし
