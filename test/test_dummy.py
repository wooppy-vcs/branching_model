from features.alpha import Alpha


def test_dummy():
    assert 1 == 1


def test_alpha():
    number = 10
    a = Alpha(number)
    assert number == a.get_number()