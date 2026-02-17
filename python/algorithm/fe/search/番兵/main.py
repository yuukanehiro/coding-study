
# 番兵
def get_answer(a: list, x: int) -> bool:
    # 要素数
    n = len(a)

    # 番兵をpush
    a.append(x)

    count = 0
    for i in a:
        count += 1
        if a[i] == x:
            break
    
    if count < n:
        return True
    else:
        return False

def main():
    x = int(input())
    a = [3, 4, 5, 11, 15, 16]

    res = get_answer(a, x)

    if res:
        print("存在する")
    else:
        print("存在しない")

def test():
    in1 = 3
    a1 = [1, 2, 3, 4, 5]
    expect1 = True
    assert get_answer(a1, in1) == expect1

    in2 = 9
    a2 = [1, 2, 3, 4, 5]
    expect2 = False
    assert get_answer(a2, in2) == expect2

test()
main()
