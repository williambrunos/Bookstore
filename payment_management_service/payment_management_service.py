from flask import Flask, jsonify, request
from commons.api_config import HTTP_STATUS_CREATED, HTTP_STATUS_FAILURE, HTTP_STATUS_SUCCESS, PAYMENT_MANAGEMENT_PORT

app = Flask(__name__)
payments = []

@app.route('/payments', methods='POST')
def process_payment():
    payment_data = request.get_json()
    payment = {
        'oder_id': payment_data['order_id'],
        'user_id': payment_data['user_id'],
        'price': payment_data['price']
    }
    payments.append(payment)
    
    return jsonify(payment), HTTP_STATUS_SUCCESS


if __name__ == '__main__':
    app.run(port=PAYMENT_MANAGEMENT_PORT)
    