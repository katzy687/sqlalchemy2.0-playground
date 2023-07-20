from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:///sample.db", echo=True)

# for Core style usage, ORM does this implicitly
metadata_obj = MetaData()