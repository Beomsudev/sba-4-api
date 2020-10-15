from bumsu_sba_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Item(Base):
    def __init__(self):
        __tablename__ = "items"
        
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String)
        price = Column(String)