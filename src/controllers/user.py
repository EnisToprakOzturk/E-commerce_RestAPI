from flask_restful import Resource, abort, reqparse, Api
from models.user import *
from app import app

api = Api(app)

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("userName",type=str, help="name of the user", required=True)
user_put_args.add_argument("userSurname",type=str, help="Surname of the user", required=True)
user_put_args.add_argument("password", type=str, help="Password of the user", required=True)
user_put_args.add_argument("email", type=str, help="Email of the user", required=True)
user_put_args.add_argument("phone", type=str, help="Phone number of the user", required=True)
user_put_args.add_argument("birthday", type=str, help="Birthday of the user", required=True)

class User(Resource):

    """"
    def get(self, user_id):
        result = UserModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, massage="Could not find user with that id..")
        return result 
    """
    def put(self):
        args = user_put_args.parse_args()
        """"
        result = UserModel.query.filter_by(id=user_id).first()
        if result:
            abort(409, message="User id taken...") """

        user = UserModel(userName=args['userName'],
        userSurname=args['userSurname'], password=args['password'],
        email=args['email'], phone=args['phone'], birthday=args['birthday'])
        db.session.add(user)
        db.session.commit()
        return user, 201

api.add_resource(User, "http://127.0.0.1:5000/user")