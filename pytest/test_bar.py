def bar():
    return "bar"


class TestBar:
    def test_bar_returns_bar(self):
        assert bar() == "bar"

    def test_bar_does_not_return_foo(self):
        assert bar() != "foo"
