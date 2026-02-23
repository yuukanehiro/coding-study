

def get_answer(a: list[int]) -> list[int]:
    n = len(a)
    gap = n // 2

    while gap > 0:
        for i in range(gap, len(a)):
            tmp = a[i]
            j = i
            while j >= gap and a[j - gap] > tmp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = tmp
        gap = gap // 2

    return a

def test():
    a = [4, 3, 2, 1]
    expect = [1, 2, 3, 4]
    assert get_answer(a) == expect

test()

# gap ... 2
# i = 2の時
# tmp = a[i] ... 2
# j = 2

# 2 >= 2 and a[2 - 2] > tmp // a[0] > a[2] // 4 > 2
#     a[2] = a[0] // [4, 3, 4, 1]
#     j -= gap // j ... 2 - 2 = 0になるので j>= gap 0>= 2が成立しないのでwhile終了

#     a[2] = 2 // [4, 3, 2, 1]

# i = 3の時
# tmp = a[3] ... 1
# j = 3
# while j >= gap and a[j - gap] > tmp: // while 3 >= 2 and a[3 - 2] > a[3] // a[1] > a[3] // 3 > 1
#     a[j] = a[j - gap] // a[3] = a[3 - 2] // [4, 3, 2, 3]
#     j -= gap // 2 - 1 = 1 j ... 1

# 1>=2が成立しないのでwhile終了
#     a[j] = tmp // [4, 3, 2, 3] -> [4, 1, 2, 3]





