"""empty message

Revision ID: c2848a33422e
Revises: c0b483f1d366
Create Date: 2021-08-23 15:17:02.080669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2848a33422e'
down_revision = 'c0b483f1d366'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('member_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_question_user_id_member', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_question_member_id_member'), 'member', ['member_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), server_default=sa.text("'1'"), nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_question_member_id_member'), type_='foreignkey')
        batch_op.create_foreign_key('fk_question_user_id_member', 'member', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('member_id')

    # ### end Alembic commands ###
