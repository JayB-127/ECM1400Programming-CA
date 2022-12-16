import utils

def test_sumvalues():
    assert utils.sumvalues([1, 3, 2]) == 6

def test_maxvalue():
    assert utils.maxvalue([1, 3, 2]) == 1

def test_minvalue():
    assert utils.minvalue([1, 3, 2]) == 0

def test_meanvalue():
    assert utils.meannvalue([1, 3, 2]) == 2

def test_countvalue():
    assert utils.countvalue([1, 3, 2, 3], 3) == 2