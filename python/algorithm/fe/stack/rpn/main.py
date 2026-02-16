"""
逆ポーランド記法（後置記法）の計算
通常: 3 + 4
後置: 3 4 +
"""


def get_answer(expression: list) -> int:
    stack = []

    for token in expression:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a // b

            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()


def main():
    # スペース区切りで入力: 3 4 +
    tokens = input().split()
    res = get_answer(tokens)
    print(res)


def test():
    # 3 + 4 = 7
    in1 = ["3", "4", "+"]
    expect1 = 7
    assert get_answer(in1) == expect1

    # (3 + 4) * 2 = 14
    in2 = ["3", "4", "+", "2", "*"]
    expect2 = 14
    assert get_answer(in2) == expect2

    # 5 + ((1 + 2) * 4) - 3 = 14
    in3 = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    expect3 = 14
    assert get_answer(in3) == expect3

    # 10 - 3 = 7
    in4 = ["10", "3", "-"]
    expect4 = 7
    assert get_answer(in4) == expect4


test()
main()
