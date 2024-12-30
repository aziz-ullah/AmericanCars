from marshmallow_sqlalchemy import SQLAlchemySchema
from app.models.user import User
from marshmallow import fields,Schema
from marshmallow import fields, Schema, validates, ValidationError

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User

    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(load_only=True, required=True)
    role = fields.String(required=True)
    
    @validates('role')
    def validate_role(self, value):
        if value not in ['superadmin','admin', 'user', 'viewer']:
            raise ValidationError('Invalid role. Roles must be super admin,admin, user, or viewer.')
    
class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String( required=True)
    
class UpdateUserSchema(Schema):
    id = fields.Integer(required=True)
    username = fields.String()
    password = fields.String(load_only=True)
    role = fields.String()