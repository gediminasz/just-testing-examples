from unittest import TestCase

def foo():
    return "foo"

class FooTestCase(TestCase):
    def test_foo_returns_foo(self):
        self.assertEqual(foo(), "foo")

    def test_foo_does_not_return_bar(self):
        self.assertNotEqual(foo(), "bar")
