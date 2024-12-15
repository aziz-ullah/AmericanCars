from functools import wraps
from flask import request, jsonify

def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Example role extraction from request
            user_role = request.headers.get('Role')
            if user_role not in allowed_roles:
                return jsonify({"error": "Access forbidden"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
