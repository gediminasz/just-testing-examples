from unittest import TestCase

def bar():
    return "bar"

class BarTestCase(TestCase):
    def test_bar_returns_bar(self):
        self.assertEqual(bar(), "bar")

    def test_bar_does_not_return_foo(self):
        self.assertNotEqual(bar(), "foo")
