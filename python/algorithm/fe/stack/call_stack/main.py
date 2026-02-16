"""
関数呼び出しのシミュレーション（コールスタック）
関数呼び出し時にスタックに積み、戻り時に取り出す
"""


def simulate(functions: list) -> list:
    """
    関数呼び出し順を受け取り、戻り順を返す
    """
    stack = []
    result = []

    for func in functions:
        stack.append(func)

    while stack:
        result.append(stack.pop())

    return result


def get_answer(functions: list) -> str:
    return " -> ".join(simulate(functions))


def main():
    # スペース区切りで入力: main funcA funcB funcC
    functions = input().split()
    print("呼び出し順:", " -> ".join(functions))
    print("戻り順:    ", get_answer(functions))


def test():
    in1 = ["main", "funcA", "funcB"]
    expect1 = ["funcB", "funcA", "main"]
    assert simulate(in1) == expect1

    in2 = ["A", "B", "C", "D"]
    expect2 = ["D", "C", "B", "A"]
    assert simulate(in2) == expect2


test()
main()
