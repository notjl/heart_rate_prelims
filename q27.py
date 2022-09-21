from tempfile import TMP_MAX
from flask import Flask, jsonify, request

import json

app = Flask(__name__)


@app.route('/heart/get', methods=['GET'])
def get_hearts():
    with open('hearts.json', 'r') as f:
        return jsonify(json.load(f))

@app.route('/heart/create', methods=['POST'])
def create_heart():
    with open('hearts.json', 'r') as f:
        hearts = json.load(f)
    
    heart = request.get_json()
    hearts.append(heart)

    with open('hearts.json', 'w') as fw:
        json.dump(hearts, fw)

    return jsonify(hearts), 200

@app.route('/heart/<int:id>', methods=['GET'])
def get_heart(id):
    with open('hearts.json', 'r') as f:
        hearts = json.load(f)

    for heart in hearts:
        if heart['heart_id'] == id:
            return jsonify(heart), 200

@app.route('/heart/update/<int:id>', methods=['POST'])
def update_heart(id):
    with open('hearts.json', 'r') as f:
        hearts = json.load(f)

    for index, heart in enumerate(hearts):
        if heart['heart_id'] == id:
            hearts[index] = request.get_json()
            break

    with open('hearts.json', 'w') as fw:
        json.dump(hearts, fw)
    
    return jsonify(hearts), 200
    
@app.route('/heart/delete/<int:id>', methods=['POST'])
def delete_heart(id):
    with open('hearts.json', 'r') as f:
        hearts = json.load(f)

    for index, heart in enumerate(hearts):
        if int(heart['heart_id']) == id:
            hearts.pop(index)

    with open('hearts.json', 'w') as fw:
        json.dump(hearts, fw)

    return jsonify(hearts), 200

if __name__ == '__main__':
    app.run(debug=True)
