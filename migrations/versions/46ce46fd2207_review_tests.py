"""review tests

Revision ID: 46ce46fd2207
Revises: 196c607d7498
Create Date: 2014-09-11 05:29:25.765065

"""

# revision identifiers, used by Alembic.
revision = '46ce46fd2207'
down_revision = '196c607d7498'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review_test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('finished', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review_test')
    ### end Alembic commands ###
