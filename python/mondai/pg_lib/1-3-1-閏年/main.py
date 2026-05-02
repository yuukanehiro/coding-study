def get_answer(n: int) -> bool:
    # 4で割切れる かつ 100で割切れない。もしくは400で割切れる == 閏年
    if n % 4 != 0:
        return False
    
    if n % 100 != 0:
        return True

    if n % 400 != 0:
        return False

    return True

def test():
    input_1 = 3
    assert get_answer(input_1) == False
    input_2 = 8
    assert get_answer(input_2) == True
    input_3 = 100
    assert get_answer(input_3) == False
    input_4 = 104
    assert get_answer(input_4) == True
    input_5 = 800
    assert get_answer(input_5) == True

test()