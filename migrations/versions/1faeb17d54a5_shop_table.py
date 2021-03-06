"""shop table

Revision ID: 1faeb17d54a5
Revises: 
Create Date: 2021-06-17 20:22:48.025081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1faeb17d54a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sum', sa.NUMERIC(), nullable=True),
    sa.Column('currency', sa.String(length=3), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('sending_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop')
    # ### end Alembic commands ###
