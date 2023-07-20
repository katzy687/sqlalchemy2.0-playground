from sqlalchemy import text
from engine import engine


def hello_world():
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())


def commit_as_you_go():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
        )
        conn.commit()


def begin_once():
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
        )


def fetch_rows():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM some_table"))
        for row in result:
            print(f"x: {row.x}  y: {row.y}")


def send_params_query(y_val: int = 2):
    """
    this is important to pass queries in like this to avoid SQL injection
    """
    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": y_val})
        for row in result:
            print(f"x: {row.x}  y: {row.y}")


if __name__ == "__main__":
    # hello_world()
    # commit_as_you_go()  # throws error for already created table
    # begin_once()
    # fetch_rows()
    send_params_query(5)
