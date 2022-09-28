# tests/food/test_fruits.py
def test_is_crisp():
    assert is_crisp(fruit="apple") #  or == True
    assert is_crisp(fruit="Apple")
    assert not is_crisp(fruit="orange")
    with pytest.raises(ValueError):
        is_crisp(fruit=None)
        is_crisp(fruit="pear")


class Fruit(object):
    def __init__(self, name):
        self.name = name


class TestFruit(object):
    @classmethod
    def setup_class(cls):
        """Set up the state for any class instance."""
        pass

    @classmethod
    def teardown_class(cls):
        """Teardown the state created in setup_class."""
        pass

    def setup_method(self):
        """Called before every method to setup any state."""
        self.fruit = Fruit(name="apple")

    def teardown_method(self):
        """Called after every method to teardown any state."""
        del self.fruit

    def test_init(self):
        assert self.fruit.name == "apple"


# Parametrize
@pytest.mark.parametrize(
    "fruit, crisp",
    [
        ("apple", True),
        ("Apple", True),
        ("orange", False),
    ],
)
def test_is_crisp_parametrize(fruit, crisp):
    assert is_crisp(fruit=fruit) == crisp


# Fixtures
@pytest.fixture
def my_fruit():
    fruit = Fruit(name="apple")
    return fruit


def test_fruit(my_fruit):
    assert my_fruit.name == "apple"