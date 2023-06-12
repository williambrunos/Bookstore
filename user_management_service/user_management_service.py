from flask import Flask, jsonfy, request
from ..commons.http_status import HTTP_STATUS_SUCCESS, HTTP_STATUS_CREATED, HTTP_STATUS_FAILURE

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
    
    return jsonfy(user), HTTP_STATUS_SUCCESS

if __name__ == '__main__':
    app.run()
