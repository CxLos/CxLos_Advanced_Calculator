import pytest
from pydantic import ValidationError
from app.schemas.base import UserCreate

@pytest.mark.unit
def test_user_create_schema_valid():
    user = UserCreate(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        username="janedoe",
        password="SecurePass123"
    )
    assert user.first_name == "Jane"
    assert user.email == "jane.doe@example.com"

@pytest.mark.unit
def test_user_create_schema_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            first_name="Jane",
            last_name="Doe",
            email="not-an-email",
            username="janedoe",
            password="SecurePass123"
        )