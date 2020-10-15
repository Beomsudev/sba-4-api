from bumsu_sba_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

class Article(Base):
    __tablename__ = "articles"
    __table_args__ = {'mysql_collate':'utf8_eneral_ci'}

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user.id"))
    item = Column(Integer, ForeignKey("item.id"))
    title = Column(VARCHAR(30))
    content = Column(VARCHAR(30))

    def __repr__(self):
        return f'Article(id\'{self.id}\',user=\'{self.user}\',\
            item=\'{self.item}\',title=\'{self.title}\'

