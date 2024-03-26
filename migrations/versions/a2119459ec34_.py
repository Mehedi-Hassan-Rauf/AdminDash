"""empty message

Revision ID: a2119459ec34
Revises: bc6ac779eae8
Create Date: 2024-03-25 15:08:46.350578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2119459ec34'
down_revision = 'bc6ac779eae8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team_member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employeeName', sa.String(length=100), nullable=True),
    sa.Column('employeeAge', sa.Integer(), nullable=True),
    sa.Column('employeeCity', sa.String(length=50), nullable=True),
    sa.Column('employeeEmail', sa.String(length=100), nullable=True),
    sa.Column('employeePhone', sa.String(length=20), nullable=True),
    sa.Column('employeePost', sa.String(length=100), nullable=True),
    sa.Column('startDate', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team_member')
    # ### end Alembic commands ###
