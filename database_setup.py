from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class EngineOil(Base):
    __tablename__ = 'engineoil'

    id = Column(Integer, primary_key=True)
    brand = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    oil_item = relationship('EngineOilItem', cascade='all, delete')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'brand': self.brand,
            'id': self.id,
        }


class EngineOilItem(Base):
    __tablename__ = 'EngineOil_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    type = Column(String(250))
    engineoil_id = Column(Integer, ForeignKey('engineoil.id'))
    engineoil = relationship(EngineOil)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'type': self.type,
        }


engine = create_engine('sqlite:///engineoil.db')


Base.metadata.create_all(engine)
