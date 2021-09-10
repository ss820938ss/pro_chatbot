"""empty message

Revision ID: c09e9573901f
Revises: 2fde050f479f
Create Date: 2021-09-10 11:45:35.011170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c09e9573901f'
down_revision = '2fde050f479f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('cartId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('cartId', name=op.f('pk_cart')),
    sa.UniqueConstraint('cartId', name=op.f('uq_cart_cartId')),
    sqlite_autoincrement=True
    )
    op.drop_table('sqlite_sequence')
    op.drop_table('Cart')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cart',
    sa.Column('cartId', sa.INTEGER(), nullable=False),
    sa.Column('userId', sa.INTEGER(), nullable=True),
    sa.Column('productId', sa.INTEGER(), nullable=True),
    sa.Column('qty', sa.INTEGER(), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.Column('image', sa.VARCHAR(length=200), nullable=True),
    sa.Column('name', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('cartId'),
    sa.UniqueConstraint('cartId', name='uq_Cart_cartId')
    )
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.drop_table('cart')
    # ### end Alembic commands ###