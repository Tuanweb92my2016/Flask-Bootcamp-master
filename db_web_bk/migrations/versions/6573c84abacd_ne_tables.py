"""ne tables

Revision ID: 6573c84abacd
Revises: 
Create Date: 2018-11-14 03:15:55.857417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6573c84abacd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
