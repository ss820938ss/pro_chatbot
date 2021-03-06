"""empty message

Revision ID: dff01d93f825
Revises: 2c254bccd26e
Create Date: 2021-08-22 12:40:50.567008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dff01d93f825'
down_revision = '2c254bccd26e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('id', sa.String(length=200), nullable=False))
    op.add_column('member', sa.Column('id', sa.String(length=200), nullable=False))
    op.create_unique_constraint(None, 'member', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'member', type_='unique')
    op.drop_column('member', 'id')
    op.drop_column('admin', 'id')
    # ### end Alembic commands ###
