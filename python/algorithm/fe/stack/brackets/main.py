"""
括弧の対応チェック
開き括弧をスタックに積み、閉じ括弧で取り出して対応を確認
"""


def get_answer(expression: str) -> bool:
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def main():
    s = input()
    res = get_answer(s)
    print("OK" if res else "NG")


def test():
    # 正しい括弧
    in1 = "(a + b) * (c - d)"
    assert get_answer(in1) == True

    in2 = "((a + b) * c)"
    assert get_answer(in2) == True

    in3 = "{[()]}"
    assert get_answer(in3) == True

    # 誤った括弧
    in4 = "(a + b * (c - d)"
    assert get_answer(in4) == False

    in5 = "{[(])}"
    assert get_answer(in5) == False

    in6 = "(()"
    assert get_answer(in6) == False


test()
main()
