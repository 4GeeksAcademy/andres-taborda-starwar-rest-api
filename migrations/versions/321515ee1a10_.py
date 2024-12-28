"""empty message

Revision ID: 321515ee1a10
Revises: 8b2d57c839b0
Create Date: 2024-12-27 08:55:59.100442

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '321515ee1a10'
down_revision = '8b2d57c839b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('typeFavorite', sa.Enum('PEOPLE', 'PLANET', name='myenum'), nullable=False))
        batch_op.drop_column('some_enum')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('some_enum', postgresql.ENUM('PEOPLE', 'PLANET', name='myenum'), autoincrement=False, nullable=False))
        batch_op.drop_column('typeFavorite')

    # ### end Alembic commands ###