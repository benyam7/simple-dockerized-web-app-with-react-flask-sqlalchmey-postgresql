import json
from sqlalchemy import MetaData, Table, Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()


class SportNewsModel(db.Model):
    __tablename__ = 'sport_news'
    title = Column(String)
    details = Column(String)
    id = Column(Integer, primary_key=True)
    shares = Column(Integer)

    def __repr__(self):
        return "<SportNewsModel(title='%s',  details='%s', id='%s, shares='%s')>" % (self.title, self.details, self.id, self.shares)


def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                # this will fail on non-encodable values, like other classes
                json.dumps(data)
                if data is not None:
                    fields[field] = data
            except TypeError:
                pass
        # a json-encodable dict
        return fields
