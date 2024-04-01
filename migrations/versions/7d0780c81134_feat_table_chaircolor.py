"""feat: table ChairColor

Revision ID: 7d0780c81134
Revises: 3d432731d594
Create Date: 2024-04-02 01:23:06.751693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d0780c81134'
down_revision: Union[str, None] = '3d432731d594'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('hex', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ChairColor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chair_id', sa.Integer(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.Column('upholstery', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['chair_id'], ['Chair.id'], ),
    sa.ForeignKeyConstraint(['color_id'], ['Color.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ChairColor')
    op.drop_table('Color')
    # ### end Alembic commands ###
