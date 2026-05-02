

def get_answer(a: int, b: int) -> int:
    while b != 0:
        gcd = b
        b = a % b
        a = gcd

    return gcd


def test():
    a_1 = 144
    b_1 = 84
    expect_1 = 12

    assert get_answer(a_1, b_1) == expect_1

test()


