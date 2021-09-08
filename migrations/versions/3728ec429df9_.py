"""empty message

Revision ID: 3728ec429df9
Revises: 318e19b5a456
Create Date: 2021-09-07 14:45:59.516543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3728ec429df9'
down_revision = '318e19b5a456'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.drop_column('Price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Price', sa.INTEGER(), nullable=True))
        batch_op.drop_column('price')

    # ### end Alembic commands ###