"""feat: table Chair

Revision ID: 964fbc16a773
Revises: 875565c3d7f5
Create Date: 2024-04-02 12:07:06.569321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '964fbc16a773'
down_revision: Union[str, None] = '875565c3d7f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Chair',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('price_on_sale', sa.Integer(), nullable=True),
    sa.Column('type', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['type'], ['ChairType.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Chair')
    # ### end Alembic commands ###