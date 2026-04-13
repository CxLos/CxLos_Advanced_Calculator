
# tests/unit/test_calculation_schema_validation.py

"""
Unit tests for validating the Calculation schemas.
"""

# ==============================================
# Imports
# ==============================================

from app.schemas.calculation import CalculationBase, CalculationType, CalculationCreate, CalculationRead
from pydantic import ValidationError

# ==============================================
# Test Cases
# ==============================================