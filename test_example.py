from example import add, subtract

def test_add():
    assert add(0, 0) == 0
    assert add(3, 5) == 8
    assert add(-2, 3) == 1