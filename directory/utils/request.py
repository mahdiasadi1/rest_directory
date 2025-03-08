from flask import request
from functools import wraps
def json_only(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not request.is_json:
            return { "error": "json only"},400
        return func(*args,**kwargs)
    return wrapper    