"""Author model is added and connected to Quote model

Revision ID: fc1d00de7648
Revises: b34f44aa1ecb
Create Date: 2024-10-22 10:47:59.623758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'fc1d00de7648'
down_revision: Union[str, None] = 'b34f44aa1ecb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('authors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    with op.batch_alter_table('quotes') as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_author_id', 'authors', ['author_id'], ['id'])

    with op.batch_alter_table('quotes') as batch_op:
        batch_op.drop_column('author_name')


def downgrade() -> None:
    with op.batch_alter_table('quotes') as batch_op:
        batch_op.add_column(sa.Column('author_name', sa.VARCHAR(), nullable=True))
        batch_op.drop_constraint('fk_author_id', type_='foreignkey')
        batch_op.drop_column('author_id')

    op.drop_table('authors')
