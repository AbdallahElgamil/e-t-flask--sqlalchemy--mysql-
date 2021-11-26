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
                teacher=payload['teacher']
                notes=payload['note']
                school=payload['school']
                stage = models.year(name=name,teacher=teacher,school=school,notes=notes)
                self.session.add(stage)
                self.session.commit()
                return {'messgae':'successfull operation'}
        except Exception as ex:
            print(str(ex))

    def delete(self,sid):
        try:
            if sid:
               deletetodo = self.session.query(models.stage).filter_by(id=sid).first()
               self.session.delete(deletetodo)
               self.session.commit()
               return {'messgae':'successfull operation'}
        except Exception as ex:
            print(str(ex))
            return {'messgae':'error occoured'}


    def get_all(self):
        try:
            records = self.session.query(models.stage).all()
            return jsonify([record.to_dict() for record in records])
        except Exception as ex:
            print(str(ex))
            return {'messgae':'error occoured'}

    def update(self,sid):
        try:
           if request.method == 'POST' and sid:
                payload=request.get_json(force=True)
                stage = self.session.query(models.stage).filter_by(sno=sid).first()
                name = payload['name']
                teacher = payload['teacher']
                scholl = payload['scholl']
                notes = payload['notes']
                stage.name=name
                stage.teacher=teacher
                stage.scholl=scholl
                stage.notes=notes
                self.session.commit()
                return {'messgae':'successfull operation'}
        except Exception as ex:
            print(str(ex))
            return {'messgae':'error occoured'}











