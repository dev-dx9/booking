"""add bookings

Revision ID: 691fa8c0787e
Revises: 90c0a664e570
Create Date: 2026-03-10 22:30:16.978095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '691fa8c0787e'
down_revision: Union[str, Sequence[str], None] = '90c0a664e570'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('date_from', sa.Date(), nullable=False),
    sa.Column('date_to', sa.Date(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('bookings')
