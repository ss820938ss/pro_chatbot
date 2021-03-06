"""empty message

Revision ID: 908991db9087
Revises: d123c5bb3fc6
Create Date: 2021-09-09 14:55:26.335422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '908991db9087'
down_revision = 'd123c5bb3fc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_sequence')
    with op.batch_alter_table('Cart', schema=None) as batch_op:
        batch_op.alter_column('cartId',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Cart', schema=None) as batch_op:
        batch_op.alter_column('cartId',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    # ### end Alembic commands ###
