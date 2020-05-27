import json
import datetime

from flask import Blueprint
from bson.objectid import ObjectId

routes = Blueprint('routes', __name__)

class JSON_Improved(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        elif isinstance(o, ObjectId):
            return str(o)
        
        return json.JSONEncoder.default(self, o)

routes.json_encoder = JSON_Improved

from .index import *
from .condition import *




