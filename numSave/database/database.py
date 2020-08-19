from sqlalchemy import create_engine, MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime

class Database:
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://user:password@localhost/test")
        self.conn = self.engine.connect()
        self.metadata = MetaData()

    def create(self):
        numbers = Table('numbers', self.metadata, Column('id', Integer(), primary_key=True, autoincrement=True), Column('nums', Integer(), nullable=False))
        self.metadata.create_all(self.engine)
        return numbers

    def insert(self, numbers, num):
        ins = numbers.insert().values(
            nums = num
        )
        return self.conn.execute(ins).inserted_primary_key

    def select(self, numbers):
        select = numbers.select()
        return self.conn.execute(select).fetchall()