from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date,NVARCHAR
from .database import Base
import datetime


class crudtMixIn:

    def to_dict(self):
        try:
            return {
                column.name: getattr(self, column.name)
                if not isinstance(
                    getattr(self, column.name), (datetime.datetime, datetime.date)
                )
                else getattr(self, column.name).isoformat()
                for column in self.__table__.columns
            }
        except Exception as ex:
            # log error
            raise ex
            print(str(ex))

    # records = [{'color': 'blue'}]
    def create(self,records):
        try:
            self.__table__.insert().execute(records)
        except Exception as ex:
            # log error
            raise ex
            print(str(ex))




class year(Base, crudtMixIn):
    __tablename__ = "years"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, index=True)
    start = Column(Date, index=True)
    end = Column(Date, index=True)
    notes = Column(NVARCHAR(1000))

class stage(Base, crudtMixIn):
    __tablename__ = "stages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(NVARCHAR(50), index=True)
    teacher = Column(NVARCHAR(50), index=True)
    notes = Column(NVARCHAR(1000), index=True)
    school = Column(NVARCHAR(50),index=True)
