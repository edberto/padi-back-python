from flask import jsonify

def wrap(data, message, status):
    return jsonify({
        "data": data,
        "message": message,
        "status": status,
    })