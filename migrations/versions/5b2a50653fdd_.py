"""empty message

Revision ID: 5b2a50653fdd
Revises: 09cb29a782b6
Create Date: 2021-09-09 14:50:15.904229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b2a50653fdd'
down_revision = '09cb29a782b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cart',
    sa.Column('cartId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('cartId', 'productId', name=op.f('pk_Cart')),
    sa.UniqueConstraint('cartId', name=op.f('uq_Cart_cartId')),
    sqlite_autoincrement=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Cart')
    # ### end Alembic commands ###