import os


def test_env_var():
    assert os.environ["SPAM"] == "ham"
