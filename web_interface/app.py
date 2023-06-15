import requests
from commons.api_config import HTTP_STATUS_CREATED, HTTP_STATUS_SUCCESS, USER_MANAGEMENT_PORT, ORDER_MANAGEMENT_PORT

user_data = {
    'name': 'William',
    'email': 'william@ufc',
    'address': 'Rua rua',
    'phone_number': '123-444-555'
}

response = requests.post(f'http://localhost:{USER_MANAGEMENT_PORT}/users', json=user_data)

if response.status_code == HTTP_STATUS_SUCCESS:
    user = response.json()
    print(f'Usuário criado! \n{user}')
else:
    print('Erro durante a criação do usuário!')
    
order_data = {
    'order_id': 1,
    'user_id': 1,
    'items': '5 books',
    'status': 'payed'
}

response = requests.post(f'http://localhost:{ORDER_MANAGEMENT_PORT}/orders', json=order_data)

if response.status_code == HTTP_STATUS_CREATED:
    order = response.json()
    print(f'Pedido criado! \n{order}')
else:
    print('Erro durante a criação do pedido!')