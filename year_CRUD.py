from flask import request,jsonify
from . import models
class CRUD():
    def __init__(self,session):
        self.session=session
    def create(self):
        try:
            if request.method=='POST':
                payload=request.get_json(force=True)
                name=payload['name']
                start=payload['start']
                end=payload['end']
                notes=payload['notes']
                year = models.year(name=name,start=start,end=end,notes=notes)
                self.session.add(year)
                self.session.commit()
                return {'messgae':'successfull operation'}
        except Exception as ex:
            print(str(ex))
            return {'messgae':'error occoured'}


    def get_all(self):
        try:
            records = self.session.query(models.year).all()
            return jsonify([record.to_dict() for record in records])
        except Exception as ex:
            print(str(ex))
            return {'messgae':'error occoured'}
