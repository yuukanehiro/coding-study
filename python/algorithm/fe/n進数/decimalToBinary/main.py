
def get_answer(n: int) -> str:
    ans = ""
    while n > 0:
        r = n % 2
        n = n // 2
        ans = str(r) + ans

    return ans

def main():
    n = int(input())
    res = get_answer(n)

    print(res)

def test():
    in1 = 13
    expect1 = "1101"
    assert get_answer(in1) == expect1
    in2 = 15
    expect2 = "1111"
    assert get_answer(in2) == expect2
    in3 = 16
    expect3 = "10000"
    assert get_answer(in3) == expect3

test()
main()
