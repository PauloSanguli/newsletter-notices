"""models for all entityes"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy.dialects import postgresql as post

from datetime import datetime

import os



engine = create_engine(os.getenv("DATABASE_URI"))
metadata = MetaData()

newspapper = Table(
    "newspapper",
    metadata,
    Column("id", post.INTEGER, autoincrement=True, primary_key=True),
    Column("date_publish", post.DATE, nullable=False, default=datetime.utcnow()),
    Column("content", post.TEXT, nullable=False),
    Column("header", post.TEXT, nullable=False),
    Column("img", post.TEXT)
)

emails = Table(
    "emails",
    metadata,
    Column("id", post.INTEGER,primary_key=True, auto_increment=True),
    Column("email", post.VARCHAR(80), nullable=False, unique=True)
)
