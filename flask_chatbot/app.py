from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

def load_training_data():
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'responses.json')
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

@app.route('/get-response', methods=['GET'])
def chatbot_response():
    user_message = request.args.get('message', '').lower()
    # For demonstration, assume role is passed; else, default.
    role = request.args.get('role', 'default')
    training_data = load_training_data()
    for intent, content in training_data.items():
        if "examples" in content:
            if any(example in user_message for example in content["examples"]):
                response_dict = content["response"]
                response_text = response_dict.get(role, response_dict.get("default"))
                return jsonify({"response": response_text})
    fallback = training_data.get("fallback", {"response": "I'm sorry, I didn't understand that."})
    return jsonify({"response": fallback["response"]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
