from features.alpha import Alpha


def test_dummy():
    assert 1 == 1

    
def test_dummy_2():
    assert 10 == 10


def test_dummy_3():
    assert 20 == 20


def test_alpha():
    number = 10
    a = Alpha(number)
    assert number == a.get_number()
