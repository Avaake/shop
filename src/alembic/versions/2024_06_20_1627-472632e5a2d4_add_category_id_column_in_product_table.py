"""add category_id column in product table

Revision ID: 472632e5a2d4
Revises: 5961fc5a8fc7
Create Date: 2024-06-20 16:27:01.862857

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "472632e5a2d4"
down_revision: Union[str, None] = "5961fc5a8fc7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "products", sa.Column("category_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        op.f("fk_products_category_id_categories"),
        "products",
        "categories",
        ["category_id"],
        ["id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_products_category_id_categories"),
        "products",
        type_="foreignkey",
    )
    op.drop_column("products", "category_id")
    # ### end Alembic commands ###
