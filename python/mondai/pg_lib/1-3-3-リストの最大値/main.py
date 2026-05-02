def get_answer(l: list) -> int:
    if len(l) == 0:
        return -1

    max = l[0]
    for v in l:
        if v > max:
            max = v

    return max

def main():
    l = [10, 2, 5, 99, 80, 3]
    print(get_answer(l))

def test():
    input1 = [10, 2, 5, 99, 80, 3]
    expect1 = 99
    assert get_answer(input1) == expect1
    

test()
main()

# output:
# 99

