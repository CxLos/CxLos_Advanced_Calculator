import pytest
from app.models.user import User

# @pytest.mark.unit
# def test_hash_and_verify_password():
#     raw_password = "SecurePass123"
#     hashed = User.hash_password(raw_password)
#     assert hashed != raw_password
#     assert User.verify_password(User(password=hashed), raw_password)
