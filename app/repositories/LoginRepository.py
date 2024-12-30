from app.models.user import User
from flask_jwt_extended import create_access_token
from app.extensions import db
from datetime import timedelta

class LoginRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def login(args, session):
        username = args.get('username')
        password = args.get('password')

        user = session.query(User).filter(User.username == username).first()
  
        if not user or not user.check_password(password):
            return {'message': 'Invalid username or password'}
        
        access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=30))
        return access_token
    
    @staticmethod
    def update_user(args, session):
        user_id = args.get('id')
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return {'message': 'User not found'}, 404
        
        if 'username' in args:
            user.username = args['username']

        if 'password' in args:
            user.set_password(args['password']) 

        if 'role' in args:
            user.role = args['role']

        return {'message': 'User updated successfully'}, 200