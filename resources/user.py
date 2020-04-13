from flask import current_app, abort, request, jsonify
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import SQLAlchemyError
from models import db
from models.base import BaseModel, BaseSchema
from util import utils

baseSchema = BaseSchema()
baseSchemas = BaseSchema(many=True)

class UserProfile(Resource):
    
    def __init__(self):
        self.parser = RequestParser
    
    def get(self):
        data = request.get_json()
        isbn_number = data['isbn']
        return jsonify({'BookList': list(map(lambda base: base.serialize(), BaseModel.query.filter_by(isbn = isbn_number).all()))})
    
    def post(self):
        return utils.return_response(message='User data post')
