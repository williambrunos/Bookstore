import requests
from commons.http_status import HTTP_STATUS_CREATED, HTTP_STATUS_SUCCESS

user_data = {
    'name': 'William',
    'email': 'william@ufc',
    'address': 'Rua rua',
    'phone_number': '123-444-555'
}

response = requests.post('http://localhost:5000/users', json=user_data)

if response.status_code == HTTP_STATUS_SUCCESS:
    user = response.json()
    print(f'User created! \n{user}')
else:
    print('Error during user creation!')
    
order_data = {
    'order_id': 1,
    'user_id': 1,
    'items': '5 books',
    'status': 'payed'
}

response = requests.post('http://localhost:5002/orders', json=order_data)

if response.status_code == HTTP_STATUS_CREATED:
    order = response.json()
    print(f'Succes creating order: {order}')
else:
    print('Error during order creation!')