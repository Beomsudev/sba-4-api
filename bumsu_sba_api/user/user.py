from bumsu_sba_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

class User(Base):
    def __init__(self):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        userid = Column(String)
        userpw = Column(String)
        name = Column(String)

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.commit()