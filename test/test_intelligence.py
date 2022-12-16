from intelligence import bubble2d

def test_bubble2d():
    list1 = [[2, 1], [1, 4], [3, 2], [3, 3]]
    list2 = [[1, 4], [3, 3], [3, 2], [2, 1]]
    assert bubble2d(list1) == list2