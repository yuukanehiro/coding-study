"""
中置記法から後置記法への変換
入力: 3 + 4 * 2
出力: 3 4 2 * +
"""


def get_answer(expression: str) -> str:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    output = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        elif token in precedence:
            while (stack and
                   stack[-1] != "(" and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


def main():
    s = input()
    res = get_answer(s)
    print(res)


def test():
    in1 = "3 + 4"
    expect1 = "3 4 +"
    assert get_answer(in1) == expect1

    in2 = "3 + 4 * 2"
    expect2 = "3 4 2 * +"
    assert get_answer(in2) == expect2

    in3 = "( 3 + 4 ) * 2"
    expect3 = "3 4 + 2 *"
    assert get_answer(in3) == expect3

    in4 = "1 + 2 * 3 - 4"
    expect4 = "1 2 3 * + 4 -"
    assert get_answer(in4) == expect4


test()
main()
