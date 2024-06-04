from flask import Flask, render_template, request, jsonify
import requests
import socket

app = Flask(__name__)

API_URL = "http://localhost:8000/chat/"

@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template('index.html', hostname = hostname)

@app.route('/submit', methods=['POST'])
def submit():
    llms_name = request.form['model']
    prompt = request.form['prompt']
    output_type = request.form['output']
    payload = {
        "model": llms_name,
        "prompt": prompt
    }
    response = requests.post(f'{API_URL}{llms_name}', json = payload)
    if response.status_code == 200:
        response_data = response.json()
        if output_type == 'concise':
            return jsonify({"response": response_data.get('data', 'No response')['response']})
        else:
            return jsonify(response_data)
    else:
        return jsonify({"error": response.status_code, "message": response.text})

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)

