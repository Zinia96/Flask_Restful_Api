from flask import jsonify

admin_handle = 'admin'
admin_password = 'admin'

def return_response(message):
    return jsonify(
        {
            "message" : message
        }
    )