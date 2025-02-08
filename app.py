from flask import Flask, render_template, request, jsonify
from query_handler import QueryHandler
import os

app = Flask(__name__)
query_handler = QueryHandler()

# Ensure the database exists
if not os.path.exists('company.db'):
    from database import create_database
    create_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    user_query = data.get('query', '')
    
    try:
        response = query_handler.parse_query(user_query)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)