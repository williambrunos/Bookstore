from flask import Flask, jsonify, request
from commons.api_config import HTTP_STATUS_SUCCESS, HTTP_STATUS_CREATED, HTTP_STATUS_FAILURE, INVENTORY_MANAGEMENT_PORT

app = Flask(__name__)
books = []
stock = []

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def create_book():
    book_data = request.get_json()
    book = {
        'ISBN': book_data['ISBN'],
        'name': book_data['name'],
        'author': book_data['author'],
        'price': book_data['price']
    }
    books.append(book)
    
    return jsonify(book), HTTP_STATUS_CREATED

@app.route('/books/<string:ISBN>', methods=['DELETE'])
def delete_book(ISBN):
    book = next((book for book in books if book['ISBN'] == ISBN), None)
    
    if book:
        books.remove(book)
        return jsonify({'message': 'book deleted'})
    else:
        return jsonify({'message': 'book not found'}), HTTP_STATUS_FAILURE
    

if __name__ == '__main__':
    app.run(INVENTORY_MANAGEMENT_PORT)