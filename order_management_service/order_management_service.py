from flask import Flask, jsonify, request 
from commons.api_config import HTTP_STATUS_CREATED, HTTP_STATUS_FAILURE, HTTP_STATUS_SUCCESS, ORDER_MANAGEMENT_PORT

app = Flask(__name__)
orders = []

@app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    order_data = request.get_json()
    order = {
        'order_id': order_data['order_id'],
        'user_id': order_data['user_id'],
        'items': order_data['items'],
        'status': order_data['status']
    }
    orders.append(order)
    
    return jsonify(order), HTTP_STATUS_CREATED

if __name__ == '__main__':
    app.run(port=ORDER_MANAGEMENT_PORT)
    