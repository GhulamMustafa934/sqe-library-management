from flask import Flask, jsonify, request
import sys
import os

# Add src to the path so we can import the Library and Book classes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.library import Library, fine_tier
from src.book import Book

app = Flask(__name__)

# In-memory database for the API
library = Library()

# --- ENDPOINTS ---

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'isbn' not in data or 'author' not in data:
        return jsonify({"error": "Missing required fields: title, isbn, author"}), 400
    
    try:
        book = Book(
            title=data['title'], 
            author=data['author'], 
            isbn=data['isbn'], 
            total_copies=data.get('total_copies', 1)
        )
        library.add_book(book)
        return jsonify({"message": "Book added successfully", "isbn": book.isbn}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    if isbn not in library.books:
        return jsonify({"error": "Book not found"}), 404
    
    book = library.books[isbn]
    return jsonify({
        "title": book.title,
        "isbn": book.isbn,
        "author": book.author,
        "available_copies": book.available_copies
    }), 200

@app.route('/books', methods=['GET'])
def list_books():
    books_list = []
    for book in library.books.values():
        books_list.append({
            "title": book.title,
            "isbn": book.isbn,
            "author": book.author,
            "available_copies": book.available_copies
        })
    return jsonify(books_list), 200

@app.route('/members/<member_id>/borrow', methods=['POST'])
def borrow_book(member_id):
    data = request.get_json()
    if not data or 'isbn' not in data:
        return jsonify({"error": "Missing isbn field"}), 400
    
    try:
        library.borrow_book(member_id, data['isbn'])
        book = library.books[data['isbn']]
        return jsonify({
            "isbn": book.isbn, 
            "available_copies": book.available_copies
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/members/<member_id>/return', methods=['POST'])
def return_book(member_id):
    data = request.get_json()
    if not data or 'isbn' not in data:
        return jsonify({"error": "Missing isbn field"}), 400
    
    try:
        library.return_book(member_id, data['isbn'])
        return jsonify({"message": "Book returned successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/members/<member_id>/fines', methods=['GET'])
def get_fines(member_id):
    # For this endpoint, we'll just return a mock fine calculation based on the Lab 5 logic
    days_overdue = request.args.get('days_overdue', default=0, type=int)
    try:
        tier = fine_tier(days_overdue)
        return jsonify({
            "member_id": member_id,
            "days_overdue": days_overdue,
            "fine_tier": tier
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)