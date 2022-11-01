"""empty message

Revision ID: 55119a6d8542
Revises: 
Create Date: 2022-10-31 12:39:45.832227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55119a6d8542'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sentiment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sentiment', sa.String(length=10), nullable=False),
    sa.Column('text', sa.String(length=1000), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sentiment')
    # ### end Alembic commands ###