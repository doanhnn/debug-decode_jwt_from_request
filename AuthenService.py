from flask_jwt_extended.view_decorators import _decode_jwt_from_request
from flask import jsonify
from functools import wraps

def decode_jwt():
    try:
        jwt_data = _decode_jwt_from_request(locations= "headers", fresh=False)[0]
        return jwt_data
    except Exception as e:
        return "Permission denied! 1111111111", str(e), 403
        if str(e) == "Signature verification failed":
            return jsonify("Permission denied!2222", str(e)), 403

def authen(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            jwt_data = decode_jwt()
            return jsonify(jwt_data)
        except Exception as e:
            return jsonify("Permission denied! 4444444444", str(e)), 403
    return wrapper