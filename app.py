import sys
sys.path.append('D:/My Projects/Salman_Projects/Python')

from flask import Flask, request, jsonify
from prediction import chatbot_response


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    message = data['message']
    response = chatbot_response(message)
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000)
