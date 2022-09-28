class Method:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def do_add(self):
        return self.var1 + self.var2
    
    def do_multiple(self):
        return self.var1 * self.var2
    
import pytest

@pytest.fixture
def my_method():
    method = Method(2,3)
    return method

def test_one(my_method):
    assert my_method.do_add() == 5

def test_two(my_method):
    assert my_method.do_multiple() == 6