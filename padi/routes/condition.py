from . import routes
from .wrapper import wrap
from flask import request, jsonify
from padi.packages.condition import usecase

@routes.route('/condition/<int:label_id>', methods=['GET'])
def find_label_info(label_id):
    if label_id != 0:
        print(label_id)
        info = usecase.Usecase.find_plant_condition(label_id)
        return wrap(info, "Success", 200)
    else:
        return wrap(None, "Bad Request", 400)

