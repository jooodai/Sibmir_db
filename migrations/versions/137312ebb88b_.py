"""empty message

Revision ID: 137312ebb88b
Revises: f9f3d071e6a1
Create Date: 2020-04-07 14:34:33.377482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137312ebb88b'
down_revision = 'f9f3d071e6a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_department', table_name='user')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_fio', table_name='user')
    op.drop_index('ix_user_place', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.create_index('ix_user_place', 'user', ['place'], unique=1)
    op.create_index('ix_user_fio', 'user', ['fio'], unique=1)
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    op.create_index('ix_user_department', 'user', ['department'], unique=1)
    # ### end Alembic commands ###