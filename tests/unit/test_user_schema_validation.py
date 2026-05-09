import pytest
from pydantic import ValidationError
from app.schemas.base import UserCreate, UserBase, PasswordMixin, UserLogin


# ==============================================
# Unit Tests for UserBase
# ==============================================

@pytest.mark.parametrize(
    "first_name, last_name, email, username",
    [
        ("John",  "Doe",   "john.doe@example.com",  "johndoe"),
        ("Alice", "Smith", "alice.smith@njit.edu",  "alice123"),
        ("Bob",   "Jones", "bob@mail.com",           "bob_jones"),
    ],
    ids=[
        "user_base_john_doe",
        "user_base_alice_smith",
        "user_base_bob_jones",
    ]
)
@pytest.mark.unit
def test_user_base_valid(first_name: str, last_name: str, email: str, username: str) -> None:
    """
    Test that UserBase accepts valid user data.

    This parametrized test verifies that the UserBase schema correctly accepts
    """
    user = UserBase(
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=username,
    )

    assert user.first_name == first_name, \
        f"Expected first_name '{first_name}', got '{user.first_name}'"
    assert user.email == email, \
        f"Expected email '{email}', got '{user.email}'"
    assert user.username == username, \
        f"Expected username '{username}', got '{user.username}'"


@pytest.mark.parametrize(
    "field_overrides",
    [
        {"email":    "not-an-email"},
        {"username": "ab"},             
        {"username": "a" * 51},        
    ],
    ids=[
        "user_base_invalid_email",
        "user_base_username_too_short",
        "user_base_username_too_long",
    ]
)
@pytest.mark.unit
def test_user_base_invalid_field(field_overrides: dict) -> None:
    """
    Test that UserBase rejects invalid field values.

    This parametrized test verifies that the UserBase schema raises a
    ValidationError when any field violates its constraint (invalid email
    format, username too short, username too long).
    """
    base = {
        "first_name": "John",
        "last_name":  "Doe",
        "email":      "john.doe@example.com",
        "username":   "johndoe",
    }
    base.update(field_overrides)

    with pytest.raises(ValidationError):
        UserBase(**base)


# ==============================================
# Unit Tests for PasswordMixin
# ==============================================

@pytest.mark.unit
def test_password_mixin_valid() -> None:
    """
    Test that PasswordMixin accepts a password that meets all strength rules.
    """
    mixin = PasswordMixin(password="SecurePass123")

    assert mixin.password == "SecurePass123", \
        f"Expected 'SecurePass123', got '{mixin.password}'"


@pytest.mark.parametrize(
    "password, expected_message",
    [
        ("short",        None),                                     
        ("lowercase1",   "at least one uppercase letter"),           
        ("UPPERCASE1",   "at least one lowercase letter"),          
        ("NoDigitsHere", "at least one digit"),                    
    ],
    ids=[
        "password_too_short",
        "password_no_uppercase",
        "password_no_lowercase",
        "password_no_digit",
    ]
)
@pytest.mark.unit
def test_password_mixin_invalid(password: str, expected_message) -> None:
    """
    Test that PasswordMixin rejects passwords that violate strength requirements.

    This parametrized test covers the four strength rules enforced by the
    validate_password model validator: minimum length, uppercase letter,
    lowercase letter, and digit.
    """
    with pytest.raises(ValidationError) as excinfo:
        PasswordMixin(password=password)

    if expected_message:
        assert expected_message in str(excinfo.value), \
            f"Expected '{expected_message}' in error, got: {excinfo.value}"


# ==============================================
# Unit Tests for UserCreate (app.schemas.base)
# ==============================================

@pytest.mark.unit
def test_user_create_schema_valid() -> None:
    """
    Test that UserCreate (base) accepts valid data.
    """
    user = UserCreate(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        username="janedoe",
        password="SecurePass123"
    )

    assert user.first_name == "Jane", \
        f"Expected first_name 'Jane', got '{user.first_name}'"
    assert user.email == "jane.doe@example.com", \
        f"Expected correct email, got '{user.email}'"


@pytest.mark.unit
def test_user_create_schema_invalid_email() -> None:
    """
    Test that UserCreate (base) rejects a malformed email address.
    """
    with pytest.raises(ValidationError):
        UserCreate(
            first_name="Jane",
            last_name="Doe",
            email="not-an-email",
            username="janedoe",
            password="SecurePass123"
        )


@pytest.mark.parametrize(
    "password, expected_message",
    [
        ("short",        None),
        ("nouppercase1", "at least one uppercase letter"),
        ("NOLOWERCASE1", "at least one lowercase letter"),
        ("NoDigitsHere", "at least one digit"),
    ],
    ids=[
        "user_create_password_too_short",
        "user_create_password_no_uppercase",
        "user_create_password_no_lowercase",
        "user_create_password_no_digit",
    ]
)
@pytest.mark.unit
def test_user_create_invalid_password(password: str, expected_message) -> None:
    """
    Test that UserCreate (base) rejects passwords that fail strength requirements.
    """
    with pytest.raises(ValidationError) as excinfo:
        UserCreate(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            username="janedoe",
            password=password,
        )

    if expected_message:
        assert expected_message in str(excinfo.value), \
            f"Expected '{expected_message}' in error, got: {excinfo.value}"


# ==============================================
# Unit Tests for UserCreate (app.schemas.user)
# ==============================================

@pytest.mark.unit
def test_user_schema_create_valid() -> None:
    """
    Test that the full UserCreate schema (app.schemas.user) accepts valid data.

    The app.schemas.user.UserCreate requires confirm_password and a special
    character in addition to the base strength requirements.
    """
    from app.schemas.user import UserCreate as FullUserCreate

    user = FullUserCreate(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        username="janedoe",
        password="SecurePass123!",
        confirm_password="SecurePass123!",
    )

    assert user.first_name == "Jane"
    assert user.username == "janedoe"


@pytest.mark.unit
def test_user_schema_create_passwords_do_not_match() -> None:
    """
    Test that the full UserCreate raises a ValidationError when passwords differ.

    The verify_password_match model validator compares password and
    confirm_password and raises a ValueError if they differ.
    """
    from app.schemas.user import UserCreate as FullUserCreate

    with pytest.raises(ValidationError) as excinfo:
        FullUserCreate(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            username="janedoe",
            password="SecurePass123!",
            confirm_password="DifferentPass123!",
        )

    assert "Passwords do not match" in str(excinfo.value), \
        f"Unexpected error message: {excinfo.value}"


@pytest.mark.parametrize(
    "password, expected_message",
    [
        ("short1!",      None),                                          
        ("nouppercase1!", "at least one uppercase letter"),             
        ("NOLOWERCASE1!", "at least one lowercase letter"),            
        ("NoDigits!",    "at least one digit"),                       
        ("NoSpecial123", "at least one special character"),             
    ],
    ids=[
        "full_create_password_too_short",
        "full_create_password_no_uppercase",
        "full_create_password_no_lowercase",
        "full_create_password_no_digit",
        "full_create_password_no_special_char",
    ]
)
@pytest.mark.unit
def test_user_schema_create_invalid_password(password: str, expected_message) -> None:
    """
    Test that the full UserCreate rejects passwords failing any strength rule.

    The validate_password_strength model validator enforces five rules:
    min 8 chars, at least one uppercase, lowercase, digit, and special character.
    """
    from app.schemas.user import UserCreate as FullUserCreate

    with pytest.raises(ValidationError) as excinfo:
        FullUserCreate(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            username="janedoe",
            password=password,
            confirm_password=password,
        )

    if expected_message:
        assert expected_message in str(excinfo.value), \
            f"Expected '{expected_message}' in error, got: {excinfo.value}"


# ==============================================
# Unit Tests for UserLogin (app.schemas.base)
# ==============================================

@pytest.mark.unit
def test_user_login_valid() -> None:
    """
    Test that UserLogin accepts a valid username and password combination.
    """
    login = UserLogin(username="johndoe", password="SecurePass123")

    assert login.username == "johndoe", \
        f"Expected username 'johndoe', got '{login.username}'"


@pytest.mark.parametrize(
    "username, password",
    [
        ("jd",       "SecurePass123"), 
        ("johndoe",  "short"),         
    ],
    ids=[
        "login_username_too_short",
        "login_password_too_short",
    ]
)
@pytest.mark.unit
def test_user_login_invalid(username: str, password: str) -> None:
    """
    Test that UserLogin rejects invalid username or password values.
    """
    with pytest.raises(ValidationError):
        UserLogin(username=username, password=password)