
"""
This module defines a mixin class for SQLAlchemy models, providing common fields and functionality."""

# ==============================================
# Imports
# ==============================================

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declared_attr
from sqlalchemy.sql import func
from uuid import uuid4

# ==============================================
# Mixin Class
# ==============================================

class TimestampMixin:
  """
  Adds created_at and updated_at to any model
  """

  @declared_attr
  def created_at(cls):
    return Column(
      DateTime, 
      server_default=func.now()
    )
  
  @declared_attr
  def updated_at(cls):
    return Column(
      DateTime,
      server_default=func.now(),
      onupdate=func.now()
    )
  
class UUIDMixin:
  """
  Adds a UUID primary key to any model
  """

  @declared_attr
  def id(cls):
    return Column(
      UUID(as_uuid=True),
      primary_key=True,
      default=uuid4
    )