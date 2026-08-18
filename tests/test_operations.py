from src.math_operations import add, subtract

def test_add():
    assert add(1,2) == 3
    assert add(5,6) == 11
    
def test_sub():
    assert subtract(1,2) == -1
    assert subtract(10,6) == 4