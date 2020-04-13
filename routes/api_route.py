from flask import Blueprint
from flask_restful import Api
from resources import user, admin, search

api_route = Blueprint('api_route', __name__)

api = Api(api_route)

api.add_resource(user.UserProfile, '/user/book')
api.add_resource(admin.AdminProfile, '/admin/book')
api.add_resource(search.SearchProfile, '/book')
api.add_resource(search.CustomSearch, '/book/search')