"""empty message

Revision ID: cf676d235bcd
Revises: 807ee0e4e022
Create Date: 2021-08-22 10:57:00.571642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf676d235bcd'
down_revision = '807ee0e4e022'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'member', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'member', type_='unique')
    # ### end Alembic commands ###
