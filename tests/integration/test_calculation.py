# tests/integration/test_calculation.py

"""
Unit tests for Calculation Functions.
"""

# ==============================================
# Imports
# ==============================================

from app.models.calculation import AbstractCalculation, Calculation, Addition, Subtraction, Multiplication, Division, Power, Sqrt, Floor, Modulus
from app.schemas.calculation import CalculationType
from pydantic import ValidationError

import pytest
from uuid import uuid4

# ==============================================
# Testing Calculation Models
# ==============================================

user_id = uuid4()

# ==============================================
# Happy Path Tests
# ==============================================

def test_addition_get_result():
    """Test that Addition.get_result() returns the sum of all inputs."""
    calc = Addition(user_id=user_id, inputs=[5, 4, 12])
    assert calc.get_result() == 21

def test_subtraction_get_result():
    """
    Test that .get_result() returns the difference of all inputs.
    """
    calc = Subtraction(user_id=user_id, inputs=[13, 4])
    assert calc.get_result() == 9

def test_multiplication_get_restul():
    """
    Test that .get_result() returns the product of all inputs.
    """
    calc = Multiplication(user_id=user_id, inputs=[8,3])
    assert calc.get_result() == 24

def test_division_get_result():
    """
    Test that .get_result() returns the quotient.
    """
    calc = Division(user_id=user_id, inputs=[36,6])
    assert calc.get_result() == 6

def test_power_get_result():
    """
    Test that .get_result() returns the power of two numbers.
    """
    calc = Power(user_id=user_id, inputs=[4,2])
    assert calc.get_result() == 16

def test_sqrt_get_result():
    """
    Test that .get_result() returns the root of two numbers.
    """
    calc = Sqrt(user_id=user_id, inputs=[25])
    assert calc.get_result() == 5

def test_floor_get_result():
    """
    Test that .get_result() returns the nearest whole number of a division operation
    """
    calc = Floor(user_id=user_id, inputs=[10,3])
    assert calc.get_result() == 3

def test_modulus_get_result():
    """
    Test that .get_result() returns the remainder of a division operation
    """
    calc = Modulus(user_id=user_id, inputs=[10,3])
    assert calc.get_result() == 1

# ==============================================
# Edge Case Tests - Negative Numbers
# ==============================================

def test_addition_negative_numbers():
    """Test addition with negative numbers."""
    calc = Addition(user_id=user_id, inputs=[-5, -3])
    assert calc.get_result() == -8

def test_subtraction_negative_numbers():
    """Test subtraction with negative numbers."""
    calc = Subtraction(user_id=user_id, inputs=[-10, -4])
    assert calc.get_result() == -6

def test_multiplication_negative_numbers():
    """Test multiplication with negative numbers yields positive result."""
    calc = Multiplication(user_id=user_id, inputs=[-3, -4])
    assert calc.get_result() == 12

def test_division_negative_numbers():
    """Test division with negative numbers."""
    calc = Division(user_id=user_id, inputs=[-20, 4])
    assert calc.get_result() == -5

def test_power_negative_base():
    """Test power with a negative base."""
    calc = Power(user_id=user_id, inputs=[-2, 3])
    assert calc.get_result() == -8

def test_modulus_negative_number():
    """Test modulus with a negative dividend."""
    calc = Modulus(user_id=user_id, inputs=[-10, 3])
    assert calc.get_result() == -10 % 3

# ==============================================
# Edge Case Tests - Floats / Decimals
# ==============================================

def test_addition_floats():
    """Test addition with floating point numbers."""
    calc = Addition(user_id=user_id, inputs=[1.5, 2.3])
    assert calc.get_result() == pytest.approx(3.8)

def test_subtraction_floats():
    """Test subtraction with floats."""
    calc = Subtraction(user_id=user_id, inputs=[10.5, 3.2])
    assert calc.get_result() == pytest.approx(7.3)

def test_multiplication_floats():
    """Test multiplication with floats."""
    calc = Multiplication(user_id=user_id, inputs=[2.5, 4.0])
    assert calc.get_result() == pytest.approx(10.0)

def test_division_floats():
    """Test division with floats."""
    calc = Division(user_id=user_id, inputs=[7.5, 2.5])
    assert calc.get_result() == pytest.approx(3.0)

def test_sqrt_float():
    """Test square root with a float input."""
    calc = Sqrt(user_id=user_id, inputs=[2.25])
    assert calc.get_result() == pytest.approx(1.5)

# ==============================================
# Edge Case Tests - Zero
# ==============================================

def test_addition_with_zero():
    """Test addition with zero."""
    calc = Addition(user_id=user_id, inputs=[5, 0])
    assert calc.get_result() == 5

def test_subtraction_with_zero():
    """Test subtracting zero leaves value unchanged."""
    calc = Subtraction(user_id=user_id, inputs=[7, 0])
    assert calc.get_result() == 7

def test_multiplication_by_zero():
    """Test multiplication by zero returns zero."""
    calc = Multiplication(user_id=user_id, inputs=[100, 0])
    assert calc.get_result() == 0

def test_power_zero_exponent():
    """Test any number to the power of zero is 1."""
    calc = Power(user_id=user_id, inputs=[999, 0])
    assert calc.get_result() == 1

def test_sqrt_of_zero():
    """Test square root of zero is zero."""
    calc = Sqrt(user_id=user_id, inputs=[0])
    assert calc.get_result() == 0

def test_floor_zero_numerator():
    """Test floor division with zero numerator."""
    calc = Floor(user_id=user_id, inputs=[0, 5])
    assert calc.get_result() == 0

def test_modulus_zero_numerator():
    """Test modulus with zero numerator returns zero."""
    calc = Modulus(user_id=user_id, inputs=[0, 7])
    assert calc.get_result() == 0

# ==============================================
# Edge Case Tests - Multiple Inputs (sequential)
# ==============================================

def test_addition_multiple_inputs():
    """Test addition with more than two inputs."""
    calc = Addition(user_id=user_id, inputs=[1, 2, 3, 4, 5])
    assert calc.get_result() == 15

def test_subtraction_multiple_inputs():
    """Test subtraction with multiple sequential subtractions."""
    calc = Subtraction(user_id=user_id, inputs=[100, 10, 20, 30])
    assert calc.get_result() == 40

def test_multiplication_multiple_inputs():
    """Test multiplication with more than two inputs."""
    calc = Multiplication(user_id=user_id, inputs=[2, 3, 4])
    assert calc.get_result() == 24

def test_division_multiple_inputs():
    """Test sequential division across multiple inputs."""
    calc = Division(user_id=user_id, inputs=[100, 2, 5])
    assert calc.get_result() == pytest.approx(10.0)

# ==============================================
# Error Handling Tests - Division by Zero
# ==============================================

def test_division_by_zero_raises():
    """Test that dividing by zero raises ValueError."""
    calc = Division(user_id=user_id, inputs=[10, 0])
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.get_result()

def test_floor_division_by_zero_raises():
    """Test that floor division by zero raises ValueError."""
    calc = Floor(user_id=user_id, inputs=[10, 0])
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.get_result()

def test_modulus_by_zero_raises():
    """Test that modulus by zero raises ValueError."""
    calc = Modulus(user_id=user_id, inputs=[10, 0])
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.get_result()

def test_division_by_zero_in_sequence():
    """Test that division by zero raises even when zero is not the second input."""
    calc = Division(user_id=user_id, inputs=[100, 5, 0])
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.get_result()

# ==============================================
# Error Handling Tests - Invalid Inputs
# ==============================================

def test_addition_invalid_inputs_not_list():
    """Test that non-list inputs raise ValueError."""
    calc = Addition(user_id=user_id, inputs="not a list")
    with pytest.raises(ValueError, match="Inputs must be a list"):
        calc.get_result()

def test_addition_too_few_inputs():
    """Test that fewer than 2 inputs raises ValueError."""
    calc = Addition(user_id=user_id, inputs=[5])
    with pytest.raises(ValueError, match="at least two"):
        calc.get_result()

def test_subtraction_too_few_inputs():
    """Test that subtraction with one input raises ValueError."""
    calc = Subtraction(user_id=user_id, inputs=[5])
    with pytest.raises(ValueError, match="at least two"):
        calc.get_result()

def test_multiplication_too_few_inputs():
    """Test that multiplication with one input raises ValueError."""
    calc = Multiplication(user_id=user_id, inputs=[5])
    with pytest.raises(ValueError, match="at least two"):
        calc.get_result()

def test_division_too_few_inputs():
    """Test that division with one input raises ValueError."""
    calc = Division(user_id=user_id, inputs=[5])
    with pytest.raises(ValueError, match="at least two"):
        calc.get_result()

def test_power_too_few_inputs():
    """Test that power with one input raises ValueError."""
    calc = Power(user_id=user_id, inputs=[5])
    with pytest.raises(ValueError, match="at least 2"):
        calc.get_result()

def test_floor_too_few_inputs():
    """Test that floor division with one input raises ValueError."""
    calc = Floor(user_id=user_id, inputs=[5])
    with pytest.raises(ValueError, match="at least 2"):
        calc.get_result()

def test_modulus_too_few_inputs():
    """Test that modulus with one input raises ValueError."""
    calc = Modulus(user_id=user_id, inputs=[5])
    with pytest.raises(ValueError, match="at least 2"):
        calc.get_result()

def test_sqrt_negative_input_raises():
    """Test that square root of a negative number raises ValueError."""
    calc = Sqrt(user_id=user_id, inputs=[-4])
    with pytest.raises(ValueError, match="negative"):
        calc.get_result()

# ==============================================
# Factory Method Tests - Calculation.create()
# ==============================================

def test_factory_creates_addition():
    """Test that Calculation.create returns an Addition instance."""
    calc = Calculation.create("addition", user_id, [1, 2])
    assert isinstance(calc, Addition)
    assert calc.get_result() == 3

def test_factory_creates_subtraction():
    """Test that Calculation.create returns a Subtraction instance."""
    calc = Calculation.create("subtraction", user_id, [10, 3])
    assert isinstance(calc, Subtraction)
    assert calc.get_result() == 7

def test_factory_creates_multiplication():
    """Test that Calculation.create returns a Multiplication instance."""
    calc = Calculation.create("multiplication", user_id, [4, 5])
    assert isinstance(calc, Multiplication)
    assert calc.get_result() == 20

def test_factory_creates_division():
    """Test that Calculation.create returns a Division instance."""
    calc = Calculation.create("division", user_id, [20, 4])
    assert isinstance(calc, Division)
    assert calc.get_result() == 5

def test_factory_creates_power():
    """Test that Calculation.create returns a Power instance."""
    calc = Calculation.create("power", user_id, [3, 3])
    assert isinstance(calc, Power)
    assert calc.get_result() == 27

def test_factory_creates_sqrt():
    """Test that Calculation.create returns a Sqrt instance."""
    calc = Calculation.create("square_root", user_id, [16])
    assert isinstance(calc, Sqrt)
    assert calc.get_result() == 4

def test_factory_creates_floor():
    """Test that Calculation.create returns a Floor instance."""
    calc = Calculation.create("floor", user_id, [7, 2])
    assert isinstance(calc, Floor)
    assert calc.get_result() == 3

def test_factory_creates_modulus():
    """Test that Calculation.create returns a Modulus instance."""
    calc = Calculation.create("modulus", user_id, [7, 2])
    assert isinstance(calc, Modulus)
    assert calc.get_result() == 1

def test_factory_case_insensitive():
    """Test that Calculation.create handles mixed-case type strings."""
    calc = Calculation.create("ADDITION", user_id, [1, 2])
    assert isinstance(calc, Addition)

def test_factory_invalid_type_raises():
    """Test that Calculation.create raises ValueError for unknown types."""
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        Calculation.create("logarithm", user_id, [10, 2])

# ==============================================
# Repr Test
# ==============================================

def test_calculation_repr():
    """Test the __repr__ method of a calculation."""
    calc = Addition(user_id=user_id, inputs=[1, 2])
    assert "type=" in repr(calc)
    assert "inputs=" in repr(calc)