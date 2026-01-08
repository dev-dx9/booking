"""add users

Revision ID: d740395e1e78
Revises: 8844974265c1
Create Date: 2026-01-08 17:45:51.199295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd740395e1e78'
down_revision: Union[str, Sequence[str], None] = '8844974265c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('users')
