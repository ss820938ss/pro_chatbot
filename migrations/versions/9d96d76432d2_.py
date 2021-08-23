"""empty message

Revision ID: 9d96d76432d2
Revises: b9d5ee86bf14
Create Date: 2021-08-22 13:08:05.823158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d96d76432d2'
down_revision = 'b9d5ee86bf14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('ad_no', sa.Integer(), nullable=False))
    op.add_column('admin', sa.Column('ad_id', sa.String(length=200), nullable=False))
    op.add_column('admin', sa.Column('ad_name', sa.String(length=200), nullable=False))
    op.add_column('admin', sa.Column('ad_email', sa.String(length=200), nullable=False))
    op.add_column('admin', sa.Column('ad_password', sa.String(length=200), nullable=False))
    op.drop_column('admin', 'no')
    op.drop_column('admin', 'id')
    op.drop_column('admin', 'password')
    op.drop_column('admin', 'email')
    op.drop_column('admin', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('name', sa.VARCHAR(length=200), nullable=False))
    op.add_column('admin', sa.Column('email', sa.VARCHAR(length=200), nullable=False))
    op.add_column('admin', sa.Column('password', sa.VARCHAR(length=200), nullable=False))
    op.add_column('admin', sa.Column('id', sa.VARCHAR(length=200), nullable=False))
    op.add_column('admin', sa.Column('no', sa.INTEGER(), nullable=False))
    op.drop_column('admin', 'ad_password')
    op.drop_column('admin', 'ad_email')
    op.drop_column('admin', 'ad_name')
    op.drop_column('admin', 'ad_id')
    op.drop_column('admin', 'ad_no')
    # ### end Alembic commands ###