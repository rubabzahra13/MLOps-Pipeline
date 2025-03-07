import joblib
from sklearn.datasets import load_iris
import numpy as np

def test_model_loading():
    model = joblib.load("src/model.pkl")
    assert model is not None, "Model failed to load"

def test_model_prediction():
    model = joblib.load("src/model.pkl")
    data = load_iris()
    X_sample = np.array(data.data[:1])  # Single sample
    pred = model.predict(X_sample)
    assert len(pred) == 1, "Model did not return a prediction"
