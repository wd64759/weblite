from flask import Blueprint
from flask_restful import Resource, Api, reqparse

import json
import logging
from weblite.db.dbhelper import db_session
from weblite.db.app_model import Staff

lite_service = Blueprint('lite_router', __name__, url_prefix='/restful')
lite_api = Api(lite_service)

# validation logic
get_params = reqparse.RequestParser()
get_params.add_argument('id', type=int, dest='id')

post_params = reqparse.RequestParser()
post_params.add_argument('staff', required=True, help='update/create operations are allowed based on json object')

_EMPTY_RESULT = {}

class LoginService(Resource):

    logger = logging.getLogger('LoginService')
    session = db_session

    def get(self):
        self.logger.info('receive the get request')
        staffs = self.session.query(Staff).orderby(Staff.name).limit(100).all()
        if len(staffs == 0):
            return _EMPTY_RESULT




class StaffsService(Resource):

    def get(self):
        # TODO: operation against staffs , query criteria comes from get_params
        pass


class StaffDetailService(Resource):

    def get(self, sid):
        # TODO: get specific staff info
        pass

    def post(self, sid):
        # TODO: add new staff
        pass

    def update(self, sid):
        # TODO: update existing one by id
        pass

    def delete(self, sid):
        # TODO: remove existing one by id
        pass


lite_api.add_resource(LoginService, '/login')
lite_api.add_resource(StaffsService, '/staff/<int:id>')
lite_api.add_resource(StaffDetailService, '/staffs')

