from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Mock data for bolt tightness
def generate_mock_data():
    return [
        {"bolt_id": f"Bolt-{i+1}", "tightness": random.randint(70, 130), 
         "status": "Optimal" if 90 <= random.randint(70, 130) <= 110 else "Critical"}
        for i in range(10)
    ]

@app.route('/api/bolts', methods=['GET'])
def get_bolts():
    data = generate_mock_data()
    return jsonify(data)

# Serve frontend
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)