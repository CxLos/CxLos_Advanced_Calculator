
"""
Unit tests for configuration settings.
"""

# ==============================================
# Imports
# ==============================================

from app.core.config import Settings, get_settings

# ==============================================
# Test Cases
# =============================================

def test_get_settings():
  """
  Verify the get settings function works
  """

  result = get_settings()
  assert isinstance(result, Settings)