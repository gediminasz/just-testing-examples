from foo import foo


def test_foo_returns_foo():
    assert foo() == "foo"


def test_foo_does_not_return_bar():
    assert foo() != "bar"
