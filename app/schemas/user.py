
# ==================================
# Imports
# ==================================

from datetime import datetime
from typing import Optional
from datetime import datetime
# --------------------------------
import uuid
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID
# --------------------------------
from pydantic import BaseModel, EmailStr, ConfigDict
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
# --------------------------------
from app.database import Base

# ==================================
# User Schema and Model
# ==================================

class User(Base):
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

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

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

    created_at = Column(
        DateTime,
        default=datetime.now,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False
    )

    # Relationship to calculations
    # back_populates creates a bidirectional relationship
    # cascade="all, delete-orphan" ensures calculations are deleted
    # when user is deleted
    
    calculations = relationship(
        "Calculation", # This string references the Calculation model 
        back_populates="user", # This should match the 'user' relationship in the Calculation model
        cascade="all, delete-orphan" # Ensures that when a user is deleted, all their calculations are also deleted
    )

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

# ==================================
# Authentication Schemas
# ==================================

class UserResponse(BaseModel):
    """Schema for user response data"""
    id: UUID
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)  # Enable mapping from ORM objects


class Token(BaseModel):
    """Schema for authentication token response"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
                "token_type": "bearer",
                "user": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "username": "johndoe",
                    "email": "john.doe@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "is_active": True,
                    "is_verified": False,
                    "created_at": "2025-01-01T00:00:00",
                    "updated_at": "2025-01-08T12:00:00",
                },
            }
        }
    )


class TokenData(BaseModel):
    """Schema for JWT token payload"""
    user_id: Optional[UUID] = None


class UserLogin(BaseModel):
    """Schema for user login"""
    username: str
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "johndoe123",
                "password": "SecurePass123",
            }
        }
    )
