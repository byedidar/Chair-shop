"""feat: table Wishlist

Revision ID: 674ad303d720
Revises: 41df15d86f47
Create Date: 2024-04-02 12:11:34.307000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '674ad303d720'
down_revision: Union[str, None] = '41df15d86f47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Wishlist',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('chair_id', sa.BigInteger(), nullable=True),
    sa.Column('bought_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('upholstery_color_id', sa.Integer(), nullable=True),
    sa.Column('shell_color_id', sa.Integer(), nullable=True),
    sa.Column('bought', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['chair_id'], ['Chair.id'], ),
    sa.ForeignKeyConstraint(['shell_color_id'], ['Color.id'], ),
    sa.ForeignKeyConstraint(['upholstery_color_id'], ['Color.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Wishlist')
    # ### end Alembic commands ###
