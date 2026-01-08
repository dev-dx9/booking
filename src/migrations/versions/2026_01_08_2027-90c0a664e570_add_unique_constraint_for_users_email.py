"""add unique constraint for users.email

Revision ID: 90c0a664e570
Revises: d740395e1e78
Create Date: 2026-01-08 20:27:47.110798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '90c0a664e570'
down_revision: Union[str, Sequence[str], None] = 'd740395e1e78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(None, 'users', ['email'])


def downgrade() -> None:
    op.drop_constraint(None, 'users', type_='unique')
