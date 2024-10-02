from flask import Flask, request, jsonify, send_from_directory
from g4f.client import Client
from flask_cors import CORS

app = Flask(__name__)
client = Client()
CORS(app)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}],
    )
    return jsonify({"response": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
