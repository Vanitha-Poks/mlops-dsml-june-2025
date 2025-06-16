# for using pytest, whatever python file contains the test function, it should start with test_ or end with _test.py

from base_file import add, subtract, multiply, divide


def test_first_test_of_this_lecture():
    """Test the add function."""
    a = 8
    b = 12
    assert add(a, b) == a + b, "Expected sum does not match actual sum."

    a = 25
    b = 35
    assert add(a, b) == a + b, "Expected sum does not match actual sum."

    assert add(0, 0) == 0, "Expected sum of zeroes should be zero."


def test_subtract_but_can_be_anything():
    """Test the subtract function."""
    a = 18
    b = 7
    assert (
        subtract(a, b) == a - b
    ), "Expected difference does not match actual difference."

    # assert multiply(a, b) == a * b, "Expected product does not match actual product."
    # assert divide(a, b) == a / b, "Expected quotient does not match actual quotient."


def test_multiply():
    """Test the multiply function."""
    a = 6
    b = 7
    assert multiply(a, b) == a * b, "Expected product does not match actual product."

    a = -4
    b = 8
    assert multiply(a, b) == a * b, "Expected product does not match actual product."

    assert multiply(0, 150) == 0, "Expected product with zero should be zero."


def test_divide():
    """Test the divide function."""
    a = 24
    b = 4
    assert divide(a, b) == a / b, "Expected quotient does not match actual quotient."

    a = 21
    b = 7
    assert divide(a, b) == a / b, "Expected quotient does not match actual quotient."

    try:
        divide(12, 0)
    except ValueError as e:
        assert (
            str(e) == "Cannot divide by zero."
        ), "Expected ValueError for division by zero."
    else:
        assert False, "Expected ValueError for division by zero but none was raised."
