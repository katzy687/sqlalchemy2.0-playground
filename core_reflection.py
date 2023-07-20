from engine import engine, metadata_obj
from sqlalchemy import Table


some_table = Table("some_table", metadata_obj, autoload_with=engine)
print(some_table)