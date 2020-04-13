from flask import current_app, abort, jsonify, request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import SQLAlchemyError
from models import db
from models.base import BaseModel
from util import utils

class SearchProfile(Resource):
    
    def __init__(self):
        self.parser = RequestParser
    
    def get(self):
        return jsonify({'BookList': list(map(lambda base: base.serialize(), BaseModel.query.all()))})
    
    def post(self):
        return utils.return_response(message='Search post method')

class CustomSearch(Resource):

    def __init__(self):
        self.parser = RequestParser

    def get(self):
        data = request.get_json()
        name = data['name']
        return jsonify({'BookList': list(map(lambda base: base.serialize(), BaseModel.query.filter(BaseModel.name.contains(name))))})
