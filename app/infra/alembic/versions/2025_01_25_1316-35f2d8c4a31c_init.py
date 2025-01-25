"""init

Revision ID: 35f2d8c4a31c
Revises:
Create Date: 2025-01-25 13:16:44.840586

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = '35f2d8c4a31c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user',
        sa.Column('uuid', sa.Uuid(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('password', sa.LargeBinary(), nullable=False),
        sa.PrimaryKeyConstraint('uuid'),
        sa.UniqueConstraint('username'),
    )
    op.create_table(
        'matrix',
        sa.Column('uuid', sa.Uuid(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('height', sa.Integer(), nullable=False),
        sa.Column('width', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('uuid'),
        sa.UniqueConstraint('name'),
    )
    op.create_table(
        'user_matrix',
        sa.Column('uuid', sa.Uuid(), nullable=False),
        sa.Column('user_uuid', sa.Uuid(), nullable=False),
        sa.Column('matrix_uuid', sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ['matrix_uuid'],
            ['matrix.uuid'],
        ),
        sa.ForeignKeyConstraint(
            ['user_uuid'],
            ['user.uuid'],
        ),
        sa.PrimaryKeyConstraint('uuid', 'user_uuid', 'matrix_uuid'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_matrix')
    op.drop_table('matrix')
    op.drop_table('user')
    # ### end Alembic commands ###
