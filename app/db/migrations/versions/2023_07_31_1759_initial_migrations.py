"""Initial migrations

Revision ID: 9993ad4809e6
Revises: 
Create Date: 2023-07-31 17:59:40.489730

"""
import fastapi_users_db_sqlalchemy
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9993ad4809e6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "artist",
        sa.Column("nickname", sa.String(), nullable=False),
        sa.Column("id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("time_created", sa.DateTime(), nullable=True),
        sa.Column("time_updated", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nickname"),
    )
    op.create_index(op.f("ix_artist_email"), "artist", ["email"], unique=True)
    op.create_table(
        "lesson",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("lecture_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("sheetmusic_img", sa.String(), nullable=False),
        sa.Column("time_created", sa.DateTime(), nullable=True),
        sa.Column("time_updated", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "subscription",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "type",
            sa.Enum("trial", "personal", "bundle", name="subscription_type"),
            nullable=True,
        ),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("expire_at", sa.DateTime(), nullable=False),
        sa.Column("time_created", sa.DateTime(), nullable=True),
        sa.Column("time_updated", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("nickname", sa.String(), nullable=False),
        sa.Column("id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("time_created", sa.DateTime(), nullable=True),
        sa.Column("time_updated", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nickname"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_table(
        "lecture",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("artist_id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("length_sec", sa.Integer(), nullable=False),
        sa.Column("time_created", sa.DateTime(), nullable=True),
        sa.Column("time_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["artist_id"],
            ["artist.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "oauth_account",
        sa.Column("id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
        sa.Column(
            "user_id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False
        ),
        sa.Column("oauth_name", sa.String(length=100), nullable=False),
        sa.Column("access_token", sa.String(length=1024), nullable=False),
        sa.Column("expires_at", sa.Integer(), nullable=True),
        sa.Column("refresh_token", sa.String(length=1024), nullable=True),
        sa.Column("account_id", sa.String(length=320), nullable=False),
        sa.Column("account_email", sa.String(length=320), nullable=False),
        sa.Column("time_created", sa.DateTime(), nullable=True),
        sa.Column("time_updated", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_oauth_account_account_id"),
        "oauth_account",
        ["account_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_oauth_account_oauth_name"),
        "oauth_account",
        ["oauth_name"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_oauth_account_oauth_name"), table_name="oauth_account")
    op.drop_index(op.f("ix_oauth_account_account_id"), table_name="oauth_account")
    op.drop_table("oauth_account")
    op.drop_table("lecture")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_table("subscription")
    op.drop_table("lesson")
    op.drop_index(op.f("ix_artist_email"), table_name="artist")
    op.drop_table("artist")
    op.execute("DROP TYPE subscription_type")
    # ### end Alembic commands ###