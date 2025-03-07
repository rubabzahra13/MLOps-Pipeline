from flask import Flask, request, jsonify
import joblib
import numpy as np  # ✅ Added this line to fix F821 error

app = Flask(__name__)

# Load trained model
model = joblib.load('src/model.pkl')


@app.route('/')
def home():
    return "ML Model API is Running!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)

    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
