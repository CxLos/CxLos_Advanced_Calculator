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