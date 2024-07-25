from flask import Flask, render_template, request, jsonify
from ai_service import generate_ai_response
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    ai_response = generate_ai_response(user_message)
    return jsonify({'message': ai_response})

if __name__ == '__main__':
    app.run(debug=True)