"""feat: table Review

Revision ID: 5f8070f86ee7
Revises: 01a1748710fa
Create Date: 2024-04-02 12:08:52.264651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f8070f86ee7'
down_revision: Union[str, None] = '01a1748710fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Review',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('star', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('chair_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chair_id'], ['Chair.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Review')
    # ### end Alembic commands ###
