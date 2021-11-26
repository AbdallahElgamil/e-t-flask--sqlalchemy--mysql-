from flask import Flask, _app_ctx_stack, jsonify, url_for
from flask_cors import CORS
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import text
from . import models,year_CRUD,stage_Crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
try:
    app = Flask(__name__)
    CORS(app)
    app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
except Exception as ex:
    print(ex)


@app.route("/year_add",methods=['POST'])
def year_create():
    CRUD=year_CRUD.CRUD(app.session)
    return CRUD.create()

@app.route("/year_getall",methods=['Get'])
def year_getall():
    CRUD=year_CRUD.CRUD(app.session)
    CRUD.get_all()

@app.route("/stage_getall",methods=['Get'])
def stage_getall():
    CRUD=stage_Crud.CRUD(app.session)
    CRUD.get_all()

@app.route("/stage_add",methods=['POST'])
def stage_create():
    CRUD=stage_Crud.CRUD(app.session)
    CRUD.create()

@app.route("/stage_delete/<int:sid>")
def stage_delete(sid):
    CRUD=stage_Crud.CRUD(app.session)
    CRUD.delete()

@app.route("/stage_update/<int:sid>",methods=['POST'])
def update_todo(sid):
    CRUD=stage_Crud.CRUD(app.session)
    CRUD.update()




@app.route("/")
def test():
     CRUD=year_CRUD.CRUD(app.session)
     return CRUD.create({ 'name' :2019, 'start' : '2019-1-1','end' :  '2019-5-1' ,'notes' : 'notes'})
#     models.year.create([{ 'name' :2019, 'start' : '2019-1-1','end' :  '2019-5-1' ,'notes' : 'notes'}])
#     # records = app.session.query(models.year).all()
#     # return jsonify([record.to_dict() for record in records])
#     # return app.session.query(text("SELECT '' ")).all()
#     # return f"See the data at {url_for('show_records')} "
#
#
# @app.route("/records/")
# def show_records():
#     records = app.session.query(models.Record).all()
#     return jsonify([record.to_dict() for record in records])


@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()
