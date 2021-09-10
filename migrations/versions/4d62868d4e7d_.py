"""empty message

Revision ID: 4d62868d4e7d
Revises: cd0f72678b2b
Create Date: 2021-09-10 11:49:12.423395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d62868d4e7d'
down_revision = 'cd0f72678b2b'
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
    sa.UniqueConstraint('cartId', name=op.f('uq_cart_cartId'))
    )
    op.drop_table('sqlite_sequence')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.drop_table('cart')
    # ### end Alembic commands ###
