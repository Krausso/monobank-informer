"""token -> api_token

Revision ID: 9537c388f494
Revises: 85125576b291
Create Date: 2021-05-09 22:52:41.363835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9537c388f494'
down_revision = '85125576b291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('token', sa.VARCHAR(length=128), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###
