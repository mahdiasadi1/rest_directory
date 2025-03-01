import os
class Base(object):
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMI_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATION=False
class Development(Base):
    pass
class Production(Base):
    pass