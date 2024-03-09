"""migrate

Revision ID: 2635fa5ea9aa
Revises: 
Create Date: 2024-03-09 22:19:36.192243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql as post

from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '2635fa5ea9aa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "newspapper",
        sa.Column("id", post.INTEGER, autoincrement=True, primary_key=True),
        sa.Column("date_publish", post.DATE, nullable=False, default=datetime.utcnow()),
        sa.Column("content", post.TEXT, nullable=False),
        sa.Column("header", post.TEXT, nullable=False),
        sa.Column("img", post.TEXT)
    )

    op.create_table(
        "emails",
        sa.Column("id", post.INTEGER,primary_key=True, autoincrement=True),
        sa.Column("email", post.VARCHAR(80), nullable=False, unique=True)
    )

def downgrade() -> None:
    pass
