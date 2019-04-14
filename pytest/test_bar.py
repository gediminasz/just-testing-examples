def bar():
    return "bar"

def test_bar_returns_bar():
    assert bar() == "bar"

def test_bar_does_not_return_foo():
    assert bar() != "foo"
