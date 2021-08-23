"""empty message

Revision ID: 6643fbdfd88a
Revises: fe849b585e25
Create Date: 2021-08-23 15:35:12.451049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6643fbdfd88a'
down_revision = 'fe849b585e25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_answer')
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('member_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_answer_user_id_member', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_answer_member_id_member'), 'member', ['member_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('user_id')

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

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), server_default=sa.text("'1'"), nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_answer_member_id_member'), type_='foreignkey')
        batch_op.create_foreign_key('fk_answer_user_id_member', 'member', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('member_id')

    op.create_table('_alembic_tmp_answer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('member_id', sa.INTEGER(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=True),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], name='fk_answer_member_id_member', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###