# app/models/user.py
"""
User Model

This module defines the User model which represents users in the system.
Each user can have multiple calculations associated with them.
"""

from sqlalchemy import Column, String, Boolean, or_
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.mixin import TimestampMixin, UUIDMixin

class User(UUIDMixin, TimestampMixin, Base):
    """
    User model representing a user in the system.
    
    A user can create and own multiple calculations. This model uses UUID
    for the primary key to ensure uniqueness across distributed systems.
    
    Attributes:
        id: Unique identifier for the user (UUID)
        username: Unique username for the user
        email: User's email address
        created_at: Timestamp when the user was created
        updated_at: Timestamp when the user was last updated
        calculations: Relationship to all calculations owned by this user
    """
    __tablename__ = 'users'

    # Primary key and identifying fields
    username = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )
    email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )
    password = Column(String, nullable=False)

    # Personal information
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    # Status flags
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    # Relationship to calculations
    # back_populates creates a bidirectional relationship
    # cascade="all, delete-orphan" ensures calculations are deleted
    # when user is deleted
    calculations = relationship(
        "Calculation",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    @classmethod
    # def register(cls, db, user_data: dict):
    #     """
    #     Register a new user.

    #     Args:
    #         db: SQLAlchemy database session
    #         user_data: Dictionary containing user registration data
            
    #     Returns:
    #         User: The newly created user instance
            
    #     Raises:
    #         ValueError: If password is invalid or username/email already exists
    #     """
    #     password = user_data.get("password")
    #     if not password or len(password) < 6:
    #         raise ValueError("Password must be at least 6 characters long")
        
    #     # Check for duplicate email or username
    #     existing_user = db.query(cls).filter(
    #         or_(cls.email == user_data["email"], cls.username == user_data["username"])
    #     ).first()
    #     if existing_user:
    #         raise ValueError("Username or email already exists")
        
    #     # Create new user instance
    #     hashed_password = cls.hash_password(password)
    #     user = cls(
    #         first_name=user_data["first_name"],
    #         last_name=user_data["last_name"],
    #         email=user_data["email"],
    #         username=user_data["username"],
    #         password=hashed_password,
    #         is_active=True,
    #         is_verified=False
    #     )
    #     db.add(user)
    #     return user

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
