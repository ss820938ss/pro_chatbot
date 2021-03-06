"""empty message

Revision ID: 0ed5816d3fbd
Revises: dff01d93f825
Create Date: 2021-08-22 12:41:17.919856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ed5816d3fbd'
down_revision = 'dff01d93f825'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('id', sa.String(length=200), nullable=False))
    op.create_unique_constraint(None, 'member', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'member', type_='unique')
    op.drop_column('member', 'id')
    # ### end Alembic commands ###
