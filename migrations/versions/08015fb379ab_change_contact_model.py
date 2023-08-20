"""change contact model

Revision ID: 08015fb379ab
Revises: 2f07de6f3433
Create Date: 2023-08-20 20:04:20.770233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08015fb379ab'
down_revision: Union[str, None] = '2f07de6f3433'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'contacts', ['personal_phone'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='unique')
    # ### end Alembic commands ###
