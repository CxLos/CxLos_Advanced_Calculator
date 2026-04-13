import pytest
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.base import UserCreate

# @pytest.mark.integration
# def test_user_uniqueness_constraint(db_session: Session):
#     user_data = {
#         "first_name": "John",
#         "last_name": "Smith",
#         "email": "john.smith@example.com",
#         "username": "johnsmith",
#         "password": "SecurePass123"
#     }
#     user1 = User.register(db_session, user_data)
#     db_session.commit()
#     with pytest.raises(Exception):
#         User.register(db_session, user_data)