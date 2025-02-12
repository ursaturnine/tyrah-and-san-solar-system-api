"""check

Revision ID: 46eb1a9e810f
Revises: 7e79df43c700
Create Date: 2022-05-06 05:06:22.867657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46eb1a9e810f'
down_revision = '7e79df43c700'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('has_moon', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
