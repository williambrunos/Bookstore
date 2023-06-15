from flask import Flask, jsonify, request
from commons.api_config import HTTP_STATUS_SUCCESS, HTTP_STATUS_CREATED, HTTP_STATUS_FAILURE, USER_MANAGEMENT_PORT

app = Flask(__name__)
users = []

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user = {
        'user_id': len(users) + 1,
        'name': user_data['name'],
        'email': user_data['email'],
        'address': user_data['address'],
        'phone_number': user_data['phone_number']
    }
    users.append(user)
    
    return jsonify(user), HTTP_STATUS_SUCCESS

if __name__ == '__main__':
    app.run(port=USER_MANAGEMENT_PORT)
