
# tests/unit/test_calculation_schema_validation.py

"""
Unit tests for validating the Calculation schemas.
"""

# ==============================================
# Imports
# ==============================================

import pytest
from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError
from app.schemas.calculation import (
    CalculationBase,
    CalculationCreate,
    CalculationUpdate,
    CalculationRead,
    CalculationType,
)

# ==============================================
# Unit Tests for CalculationType Enum
# ==============================================

@pytest.mark.parametrize(
    "value",
    [
        "addition",
        "subtraction",
        "multiplication",
        "division",
        "power",
        "sqrt",
        "modulus",
        "floor",
    ],
    ids=[
        "type_addition",
        "type_subtraction",
        "type_multiplication",
        "type_division",
        "type_power",
        "type_sqrt",
        "type_modulus",
        "type_floor",
    ]
)
def test_calculation_type_valid_values(value: str) -> None:
    """
    Test that all valid CalculationType enum values are accepted.

    This parametrized test verifies that each of the eight supported operation
    types can be used to construct a CalculationBase schema without error.

    Parameters:
    - value (str): A valid calculation type string.

    Steps:
    1. Build a CalculationBase with the given type and safe inputs.
    2. Assert that the schema's type attribute equals the expected string.
    """
    calc = CalculationBase(type=value, inputs=[4.0, 2.0])

    assert calc.type == value, f"Expected type '{value}', got '{calc.type}'"


@pytest.mark.parametrize(
    "value",
    [
        "ADDITION",
        "Subtraction",
        "MULTIPLICATION",
        "Division",
    ],
    ids=[
        "case_addition_upper",
        "case_subtraction_mixed",
        "case_multiplication_upper",
        "case_division_mixed",
    ]
)
def test_calculation_type_case_insensitive(value: str) -> None:
    """
    Test that the type field validator normalises the value to lowercase.

    The @field_validator on CalculationBase calls v.lower() before the Enum
    check, so 'ADDITION' should be accepted and stored as 'addition'.
    """
    calc = CalculationBase(type=value, inputs=[4.0, 2.0])

    assert calc.type == value.lower(), \
        f"Expected type '{value.lower()}', got '{calc.type}'"


# ==============================================
# Unit Tests for CalculationBase — Valid Inputs
# ==============================================

@pytest.mark.parametrize(
    "calc_type, inputs, expected_len",
    [
        ("addition",       [1.0, 2.0, 3.0], 3), 
        ("subtraction",    [10.0, 4.0],      2),  
        ("multiplication", [2.0, 3.0],       2),  
        ("power",          [2.0, 8.0],       2),  
        ("sqrt",           [25.0, 0.0],      2),   
    ],
    ids=[
        "base_addition_three_inputs",
        "base_subtraction_two_inputs",
        "base_multiplication_two_inputs",
        "base_power_two_inputs",
        "base_sqrt_two_inputs",
    ]
)
def test_calculation_base_valid(calc_type: str, inputs: list, expected_len: int) -> None:
    """
    Test that CalculationBase accepts valid type/inputs combinations.
    """
    calc = CalculationBase(type=calc_type, inputs=inputs)

    assert calc.type == calc_type, \
        f"Expected type '{calc_type}', got '{calc.type}'"
    assert len(calc.inputs) == expected_len, \
        f"Expected {expected_len} inputs, got {len(calc.inputs)}"


# ==============================================
# Unit Tests for CalculationBase — Invalid Type
# ==============================================

@pytest.mark.parametrize(
    "invalid_type",
    [
        "logarithm",
        "trigonometry",
        "absolute",
        "",
        123,
    ],
    ids=[
        "invalid_type_logarithm",
        "invalid_type_trigonometry",
        "invalid_type_absolute",
        "invalid_type_empty_string",
        "invalid_type_integer",
    ]
)
def test_calculation_base_invalid_type(invalid_type) -> None:
    """
    Test that CalculationBase rejects unsupported calculation types.

    The field validator raises a ValueError if the type is not one of the
    eight allowed CalculationType enum values.
    """
    with pytest.raises(ValidationError):
        CalculationBase(type=invalid_type, inputs=[1.0, 2.0])


# ==============================================
# Unit Tests for CalculationBase — Invalid Inputs
# ==============================================

def test_calculation_base_inputs_not_a_list() -> None:
    """
    Test that CalculationBase rejects a non-list inputs value.

    The check_inputs_is_list field validator raises a ValueError when
    inputs is not a list (e.g., a string or a number).
    """
    with pytest.raises(ValidationError) as excinfo:
        CalculationBase(type="addition", inputs="not-a-list")

    assert "input should be a valid list" in str(excinfo.value).lower(), \
        f"Unexpected error message: {excinfo.value}"


def test_calculation_base_too_few_inputs() -> None:
    """
    Test that CalculationBase rejects inputs with fewer than two elements.

    The model validator validate_inputs enforces a minimum of two inputs
    for every calculation type.
    """
    with pytest.raises(ValidationError):
        CalculationBase(type="addition", inputs=[5.0])


# ==============================================
# Unit Tests for CalculationBase — Division by Zero
# ==============================================

@pytest.mark.parametrize(
    "calc_type",
    [
        "division",
        "floor",
        "modulus",
    ],
    ids=[
        "div_by_zero_division",
        "div_by_zero_floor",
        "div_by_zero_modulus",
    ]
)
def test_calculation_base_division_by_zero(calc_type: str) -> None:
    """
    Test that CalculationBase rejects a zero divisor for division-like operations.

    The model validator validate_inputs checks that no element at position 1+
    is zero when the type is division, floor, or modulus.
    """
    with pytest.raises(ValidationError) as excinfo:
        CalculationBase(type=calc_type, inputs=[10.0, 0.0])

    assert "cannot divide by zero" in str(excinfo.value).lower(), \
        f"Unexpected error message: {excinfo.value}"


# ==============================================
# Unit Tests for CalculationCreate
# ==============================================

def test_calculation_create_valid() -> None:
    """
    Test that CalculationCreate accepts valid data including a UUID user_id.
    """
    user_id = uuid4()
    calc = CalculationCreate(type="multiplication", inputs=[3.0, 4.0], user_id=user_id)

    assert calc.type == "multiplication"
    assert calc.inputs == [3.0, 4.0]
    assert calc.user_id == user_id


def test_calculation_create_missing_user_id() -> None:
    """
    Test that CalculationCreate requires a user_id.
    """
    with pytest.raises(ValidationError) as excinfo:
        CalculationCreate(type="addition", inputs=[1.0, 2.0])

    assert "required" in str(excinfo.value).lower(), \
        f"Unexpected error message: {excinfo.value}"


def test_calculation_create_invalid_user_id() -> None:
    """
    Test that CalculationCreate rejects a non-UUID user_id.
    """
    with pytest.raises(ValidationError):
        CalculationCreate(type="addition", inputs=[1.0, 2.0], user_id="not-a-uuid")


# ==============================================
# Unit Tests for CalculationUpdate
# ==============================================

@pytest.mark.parametrize(
    "update_data, expected_inputs",
    [
        ({"inputs": [42.0, 7.0]},           [42.0, 7.0]),  
        ({"type": "subtraction"},            None),         
        ({},                                 None),         
    ],
    ids=[
        "update_inputs_only",
        "update_type_only",
        "update_empty",
    ]
)
def test_calculation_update_valid(update_data: dict, expected_inputs) -> None:
    """
    Test that CalculationUpdate accepts valid partial updates.

    All fields in CalculationUpdate are optional, so any combination
    (including an empty payload) must be accepted.
    """
    calc_update = CalculationUpdate(**update_data)

    assert calc_update.inputs == expected_inputs, \
        f"Expected inputs '{expected_inputs}', got '{calc_update.inputs}'"


def test_calculation_update_too_few_inputs() -> None:
    """
    Test that CalculationUpdate rejects an inputs list with fewer than two elements.

    The model validator on CalculationUpdate enforces the same minimum-two-inputs
    rule when inputs is not None.
    """
    with pytest.raises(ValidationError):
        CalculationUpdate(inputs=[5.0])