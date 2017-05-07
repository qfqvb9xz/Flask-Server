"""empty message

Revision ID: 9ad7193044aa
Revises: 9a249cfca24c
Create Date: 2017-05-07 13:45:01.284212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad7193044aa'
down_revision = '9a249cfca24c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('recommendation', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'recommendation')
    # ### end Alembic commands ###
