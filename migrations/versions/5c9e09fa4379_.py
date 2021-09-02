"""empty message

Revision ID: 5c9e09fa4379
Revises: 4d6e1574006a
Create Date: 2021-08-26 16:47:18.159050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9e09fa4379'
down_revision = '4d6e1574006a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('order_price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_price'], ['menu.menu_price'], name=op.f('fk_order_order_price_menu'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product'], ['menu.menu_no'], name=op.f('fk_order_product_menu'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('order_id', name=op.f('pk_order'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###