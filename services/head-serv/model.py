import json
from sqlalchemy import MetaData, Table, Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()


class HeadLineModel(db.Model):
    __tablename__ = 'headlines'
    title = Column(String)
    littel_description = Column(String)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<HeadLineModel(title='%s',  littel_description='%s', id='%s)>" % (self.title, self.littel_description, self.id)


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
