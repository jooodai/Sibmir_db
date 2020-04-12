"""empty message

Revision ID: b97731a27686
Revises: fc988fd52232
Create Date: 2020-04-06 21:42:16.834395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b97731a27686'
down_revision = 'fc988fd52232'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('place', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_user_place'), 'user', ['place'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_place'), table_name='user')
    op.drop_column('user', 'place')
    # ### end Alembic commands ###