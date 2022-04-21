from flask_restful import Resource, abort, reqparse
from models.user import *


user_put_args = reqparse.RequestParser()
user_put_args.add_argument("userName",type=str, help="name of the user", required=True)
user_put_args.add_argument("userSurname",type=str, help="Surname of the user", required=True)
user_put_args.add_argument("password", type=str, help="Password of the user", required=True)
user_put_args.add_argument("email", type=str, help="Email of the user", required=True)
user_put_args.add_argument("phone", type=str, help="Phone number of the user", required=True)
user_put_args.add_argument("birthday", type=str, help="Birthday of the user", required=True)






class User(Resource):

    def get(self, user_id):
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, massage="Could not find user with that id..")
        return result 

    def put(self, user_id):
