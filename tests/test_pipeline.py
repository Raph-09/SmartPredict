import os
import pytest
import pickle


MODEL_PATH = "artifacts/model_artifact/model.pkl"
def test_model():
    assert os.path.exists(MODEL_PATH), "Model file not found!"
    


# def test_example():
#     assert 1 + 1 == 2
