from bumsu_sba_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

class Item(Base):
    __tablename__ = "items"
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(30))
    price = Column(VARCHAR(30))

    def __repr__(self):
        return f'Item(id=\'{self.id}\',name=\'{self.name}\',\
            price=\'{self.price}\',)'

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(Item(name='movie', price='1000'))
query = session.query(Item).filter((Item.name == 'movie'))
print(query)
for i in query:
    print(i)
session.commit()

