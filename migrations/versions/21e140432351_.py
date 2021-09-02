"""empty message

Revision ID: 21e140432351
Revises: 5c9e09fa4379
Create Date: 2021-08-31 09:32:45.199899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21e140432351'
down_revision = '5c9e09fa4379'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('order_id', sa.INTEGER(), nullable=False),
    sa.Column('product', sa.INTEGER(), nullable=True),
    sa.Column('quantity', sa.INTEGER(), nullable=True),
    sa.Column('order_price', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['order_price'], ['menu.menu_price'], name='fk_order_order_price_menu', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product'], ['menu.menu_no'], name='fk_order_product_menu', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('order_id', name='pk_order')
    )
    # ### end Alembic commands ###
