from flask import Blueprint,jsonify
from webargs.flaskparser import use_args
from app.schemas.UserSchema import UpdateUserSchema, UserSchema, LoginSchema
from app.bl.LoginBLC import LoginBLC
from app.bl.UserBLC import UserBLC
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity, current_user
from sqlalchemy.exc import IntegrityError
from webargs import fields

bp = Blueprint('user',__name__)

@bp.route('/register', methods=['POST'])
@jwt_required()
@use_args(UserSchema(), location='json')
def add_user(args): 
    """Adding a user to Database"""
    
    if current_user.role != 'superadmin':
        return "Super Admin privileges required"
    
    try:
        result = UserBLC.add_user(args)
        
        return jsonify({"message":"User added succefully","result":result}),201
    except IntegrityError as e:
        return jsonify({"Error":e.orig.args[1]}), 422
    except Exception as e:
        return jsonify(str(e)),422
    
@bp.route('/login', methods=['POST'])
@use_args(LoginSchema(), location='json')
def login(args):
    """Login User"""
    
    try:
        result = LoginBLC.login(args)
        
        return jsonify({"result":result})
    except IntegrityError as e:
        return jsonify({"Error":e.orig.args[1]}), 422
    except Exception as e:
        return jsonify(str(e)),422
    
@bp.route('/user', methods=['PUT'])
@use_args(UpdateUserSchema(), location='json')
def update_user(args):
    """Update User"""
    
    try:
        result = LoginBLC.update_user(args)
        
        return jsonify({"result":result})
    except IntegrityError as e:
        return jsonify({"Error":e.orig.args[1]}), 422
    except Exception as e:
        return jsonify(str(e)),422
    
