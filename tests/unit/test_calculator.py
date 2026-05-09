# =============== Imports ============== #

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # what union does is it allows us to specify that a variable can be of multiple types, in this case, either int or float
from app.operations import add, subtract, multiply, divide, floor, modulus, power, sqrt  # Import the calculator functions from the operations module

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),        
        (-2, -3, -5),    
        (2.5, 3.5, 6.0),    
        (-2.5, 3.5, 1.0),   
        (0, 0, 0),           
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the 'add' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_add(2, 3, 5)
    >>> test_add(-2, -3, -5)
    """

    result = add(a, b)
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),          
        (-5, -3, -2),        
        (5.5, 2.5, 3.0),     
        (-5.5, -2.5, -3.0),  
        (0, 0, 0),           
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    This parameterized test verifies that the 'subtract' function correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.

    Parameters:
    - a (Number): The number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.

    Steps:
    1. Call the 'subtract' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(-5, -3, -2)
    """

    result = subtract(a, b)
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),          
        (-2, 3, -6),         
        (2.5, 4.0, 10.0),  
        (-2.5, 4.0, -10.0),  
        (0, 5, 0),            
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.

    This parameterized test verifies that the 'multiply' function correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.

    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.

    Steps:
    1. Call the 'multiply' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(-2, 3, -6)
    """

    result = multiply(a, b)
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           
        (-6, 3, -2.0),         
        (6.0, 3.0, 2.0),      
        (-6.0, 3.0, -2.0),    
        (0, 5, 0.0),          
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.

    This parameterized test verifies that the 'divide' function correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'divide' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_divide(6, 3, 2.0)
    >>> test_divide(-6, 3, -2.0)
    """

    result = divide(a, b)
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.

    This negative test case verifies that attempting to divide by zero raises a ValueError
    with the appropriate error message. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'divide' function with arguments 6 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_divide_by_zero()
    """

    with pytest.raises(ValueError) as excinfo:
        divide(6, 0)
    
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"


# ---------------------------------------------
# Unit Tests for the 'floor' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (7, 2, 3),         
        (-7, 2, -4),         
        (7.5, 2, 3),        
        (-7.5, 2, -4),       
        (0, 5, 0),           
    ],
    ids=[
        "floor_two_positive_integers",
        "floor_negative_integer_by_positive_integer",
        "floor_positive_float_by_positive_integer",
        "floor_negative_float_by_positive_integer",
        "floor_zero_by_positive_integer",
    ]
)
def test_floor(a: Number, b: Number, expected: int) -> None:
    """
    Test the 'floor' function with various combinations of integers and floats.

    This parameterized test verifies that the 'floor' function correctly performs floor
    division of the first number by the second, handling both positive and negative values,
    as well as integers and floats.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (int): The expected result of the floor division.

    Steps:
    1. Call the 'floor' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_floor(7, 2, 3)
    >>> test_floor(-7, 2, -4)
    """

    result = floor(a, b)
    assert result == expected, f"Expected floor({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Floor Division by Zero
# ---------------------------------------------

def test_floor_by_zero() -> None:
    """
    Test the 'floor' function with division by zero.

    This negative test case verifies that attempting to floor divide by zero raises a
    ValueError with the appropriate error message.

    Steps:
    1. Attempt to call the 'floor' function with arguments 7 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_floor_by_zero()
    """

    with pytest.raises(ValueError) as excinfo:
        floor(7, 0)

    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"


# ---------------------------------------------
# Unit Tests for the 'modulus' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 1),        
        (-10, 3, 2),     
        (10.5, 3, 1.5),      
        (0, 5, 0),         
        (7, 7, 0),           
    ],
    ids=[
        "modulus_two_positive_integers",
        "modulus_negative_integer_by_positive_integer",
        "modulus_positive_float_by_positive_integer",
        "modulus_zero_by_positive_integer",
        "modulus_equal_numbers",
    ]
)
def test_modulus(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'modulus' function with various combinations of integers and floats.

    This parameterized test verifies that the 'modulus' function correctly returns the
    remainder of dividing the first number by the second, handling both positive and
    negative values, as well as integers and floats.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (Number): The expected remainder.

    Steps:
    1. Call the 'modulus' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_modulus(10, 3, 1)
    >>> test_modulus(-10, 3, 2)
    """

    result = modulus(a, b)
    assert result == expected, f"Expected modulus({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Modulus by Zero
# ---------------------------------------------

def test_modulus_by_zero() -> None:
    """
    Test the 'modulus' function with division by zero.

    This negative test case verifies that attempting to compute the modulus with a divisor
    of zero raises a ValueError with the appropriate error message.

    Steps:
    1. Attempt to call the 'modulus' function with arguments 10 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_modulus_by_zero()
    """

    with pytest.raises(ValueError) as excinfo:
        modulus(10, 0)

    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"


# ---------------------------------------------
# Unit Tests for the 'power' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),           
        (-2, 3, -8),       
        (2, 0, 1),           
        (2, -1, 0.5),       
        (2.5, 2, 6.25),     
    ],
    ids=[
        "power_positive_base_positive_exponent",
        "power_negative_base_positive_odd_exponent",
        "power_any_base_zero_exponent",
        "power_positive_base_negative_exponent",
        "power_positive_float_base_positive_exponent",
    ]
)
def test_power(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'power' function with various combinations of bases and exponents.

    This parameterized test verifies that the 'power' function correctly raises the first
    number to the power of the second, handling positive, negative, and zero exponents,
    as well as integer and float bases.

    Parameters:
    - a (Number): The base number.
    - b (Number): The exponent.
    - expected (Number): The expected result of the exponentiation.

    Steps:
    1. Call the 'power' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_power(2, 3, 8)
    >>> test_power(2, 0, 1)
    """

    result = power(a, b)
    assert result == expected, f"Expected power({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'sqrt' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, expected",
    [
        (4, 2.0),            
        (9, 3.0),            
        (2, 2 ** 0.5),       
        (0, 0.0),            
        (2.25, 1.5),         
    ],
    ids=[
        "sqrt_perfect_square_four",
        "sqrt_perfect_square_nine",
        "sqrt_non_perfect_square",
        "sqrt_zero",
        "sqrt_perfect_square_float",
    ]
)
def test_sqrt(a: Number, expected: float) -> None:
    """
    Test the 'sqrt' function with various non-negative numbers.

    This parameterized test verifies that the 'sqrt' function correctly returns the square
    root of a non-negative number, handling both perfect squares and non-perfect squares,
    as well as integers and floats.

    Parameters:
    - a (Number): The number to find the square root of.
    - expected (float): The expected square root result.

    Steps:
    1. Call the 'sqrt' function with argument 'a'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_sqrt(4, 2.0)
    >>> test_sqrt(0, 0.0)
    """
    result = sqrt(a)
    assert result == expected, f"Expected sqrt({a}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Square Root of Negative Number
# ---------------------------------------------

def test_sqrt_negative_number() -> None:
    """
    Test the 'sqrt' function with a negative number.

    This negative test case verifies that attempting to compute the square root of a
    negative number raises a ValueError with the appropriate error message.

    Steps:
    1. Attempt to call the 'sqrt' function with argument -1, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot take the square root of a negative number!".

    Example:
    >>> test_sqrt_negative_number()
    """
    with pytest.raises(ValueError) as excinfo:
        sqrt(-1)

    assert "Cannot take the square root of a negative number!" in str(excinfo.value), \
        f"Expected error message 'Cannot take the square root of a negative number!', but got '{excinfo.value}'"
