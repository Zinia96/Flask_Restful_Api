from flask import current_app, abort, request, jsonify
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import SQLAlchemyError
from models import db
from models.base import BaseModel
from util import utils

class AdminProfile(Resource):
    
    def __init__(self):
        self.parser = RequestParser
    
    def get(self):
        return utils.return_response(message='Admin get')
    
    def post(self):
        data = request.get_json()
        
        isbn = data['isbn']
        name = data['name']
        description = data['description']
        price = data['price']
        writer = data['writer']
        handle = data['handle']
        password = data['password']


        if handle != utils.admin_handle or password != utils.admin_password:
            return utils.return_response(message='authentication error')

        model = BaseModel(isbn=isbn, name=name, description=description, price=price, writer=writer)

        try:
            db.session.add(model)
            db.session.commit()
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            db.session.rollback()
            return utils.return_response(message='Error in Database')
        else:
            return utils.return_response(message='Data inserted Ok')

    def delete(self):
        data = request.get_json()
        
        isbn_number = data['isbn']
        handle = data['handle']
        password = data['password']


        if handle != utils.admin_handle or password != utils.admin_password:
            return utils.return_response(message='authentication error')

        try:
            db.session.query(BaseModel).filter(BaseModel.isbn == isbn_number).delete()
            db.session.commit()
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            return utils.return_response(message='Error in Database')
        else:
            return utils.return_response(message='Data deleted Ok')
    
    def put(self):
        data = request.get_json()
        
        isbn_number = data['isbn']
        price = data['price']
        handle = data['handle']
        password = data['password']


        if handle != utils.admin_handle or password != utils.admin_password:
            return utils.return_response(message='Error in Database')

        try:
            model = BaseModel.query.filter(BaseModel.isbn == isbn_number).first()
            model.price = price
            db.session.flush()
            db.session.commit()
        except SQLAlchemyError as e:
            current_app.logger.error(e)
            return utils.return_response(message='Error in Database')
        else:
            return utils.return_response(message='Data updated Ok')

