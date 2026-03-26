"""add facilities

Revision ID: 97476ddd174e
Revises: 691fa8c0787e
Create Date: 2026-03-26 15:17:14.454282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '97476ddd174e'
down_revision: Union[str, Sequence[str], None] = '691fa8c0787e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('facilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room_facilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('facility_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['facility_id'], ['facilities.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('room_facilities')
    op.drop_table('facilities')
