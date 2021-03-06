from sqlalchemy import Integer, Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import json

engine = create_engine('mysql://root:root@localhost:3306', echo=True)
engine.execute("CREATE DATABASE IF NOT EXISTS autochess")
engine.execute("USE autochess")
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

json_champions_path = "%s\\sql_script\\champions.json" % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(json_champions_path) as f:
    json_data = json.load(f)
champions_data = json_data.get('champions', '')


class Champion(Base):
    __tablename__ = 'champions'
    id = Column(Integer, primary_key=True, autoincrement=1)
    name = Column(String(255))
    health = Column(Integer)
    price = Column(Integer)
    description = Column(String(255))
    rarity = Column(Integer)
    level = Column(Integer)
    img = Column(String(255))
    img_dos = Column(String(255))

    def __rep__(self):
        return "<Champion(name='%s', health='%s', price='%s', description='%s', rarity='%s', level='%s', img='%s', img_dos='%s')>" % (
            self.name, self.health, self.price, self.description, self.rarity, self.level, self.img, self.img_dos)


def get_all():
    query = session.query(Champion)
    print('query : %s' % query)
    return query.all()


Base.metadata.create_all(engine)
for champion in champions_data:
    print('champion : %s' % champion)
    champ = Champion(id=champion['id'], name=champion['name'], health=champion['health'], price=champion['price'],
                     description=champion['description'], rarity=champion['rarity'], level=champion['level'],
                     img=champion['img'], img_dos=champion['img_dos'])
    session.add(champ)

session.commit()
