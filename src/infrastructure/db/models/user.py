from sqlalchemy import Column, DateTime, String, Boolean, func

from infrastructure.db import Base, TableMixin


class User(Base, TableMixin):
    __tablename__ = 'users'

    id = Column(String(100), primary_key=True)
    username = Column(String(40), unique=True)
    first_name = Column(String(40))
    last_name = Column(String(40), nullable=True)
    email = Column(String(50), unique=True)
    password = Column(String(200))
    last_login = Column(DateTime(timezone=True), server_default=func.now())
    date_join = Column(DateTime(timezone=True), server_default=func.now())
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
