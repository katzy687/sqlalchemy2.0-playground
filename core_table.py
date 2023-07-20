from engine import engine, metadata_obj
from sqlalchemy import Table, Column, Integer, String

# Core Style table - imperative, similar to SQL
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)


def emit_table():
    metadata_obj.create_all(engine)


if __name__ == "__main__":
    emit_table()
