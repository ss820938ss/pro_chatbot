"""empty message

Revision ID: 78e39af4965d
Revises: c4b0d8f696ad
Create Date: 2021-09-07 15:18:36.459054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78e39af4965d'
down_revision = 'c4b0d8f696ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qty', sa.Integer(), nullable=True))
        batch_op.drop_column('Qty')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Qty', sa.INTEGER(), nullable=True))
        batch_op.drop_column('qty')

    # ### end Alembic commands ###
