"""create users table

Revision ID: 5961fc5a8fc7
Revises: 5cbe6254f371
Create Date: 2024-06-19 18:16:54.922437

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5961fc5a8fc7"
down_revision: Union[str, None] = "5cbe6254f371"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.VARCHAR(length=32), nullable=False),
        sa.Column("email", sa.VARCHAR(length=50), nullable=False),
        sa.Column("password", sa.LargeBinary(), nullable=False),
        sa.Column(
            "reg_time",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("role", sa.VARCHAR(length=5), server_default="user", nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("email", name=op.f("uq_users_email")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
