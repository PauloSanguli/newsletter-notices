"""change: add column category in table newspapper

Revision ID: 17a3056302ea
Revises: 2635fa5ea9aa
Create Date: 2024-03-10 02:31:59.939162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17a3056302ea'
down_revision: Union[str, None] = '2635fa5ea9aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "newspapper", 
        sa.Column("category", sa.TEXT)
    )

def downgrade() -> None:
    pass
