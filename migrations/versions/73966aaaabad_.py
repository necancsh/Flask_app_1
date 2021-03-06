"""empty message

Revision ID: 73966aaaabad
Revises: None
Create Date: 2017-02-12 23:51:30.327333

"""

# revision identifiers, used by Alembic.
revision = '73966aaaabad'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.types import Text

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('result_all', postgresql.JSON(astext_type=Text()), nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(astext_type=Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    # ### end Alembic commands ###
