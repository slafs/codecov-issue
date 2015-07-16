from my_package.my_module import my_other_function


def test_my_function():
    assert my_other_function('foo') == 'foo'
