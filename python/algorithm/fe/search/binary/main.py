# 2分探索
def get_answer(a: list[int], x: int) -> bool:
    n = len(a)

    left_index = 0
    right_index = n - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if a[mid_index] == x:
            return True
        
        if a[mid_index] < x:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return False


def main():
    a = [5, 4, 1, 2, 9, 3, 8]
    target = 9

    sortedArray = sorted(a)

    return get_answer(sortedArray, target)

def test():
    in_a1 = [5, 4, 1, 2, 9, 3, 8]
    in_a1 = sorted(in_a1)
    in_target1 = 9
    expect1 = True
    assert get_answer(in_a1, in_target1) == expect1

    in_a2 = [2, 1, 5, 6]
    in_a2 = sorted(in_a2)
    in_target2 = 999
    expect2 = False
    assert get_answer(in_a2, in_target2) == expect2

main()
test()

