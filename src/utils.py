import os
import joblib


def create_directories():
    folders = [
        'data/raw',
        'data/processed',
        'models',
        'outputs',
        'images'
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def save_model(model, filepath):
    joblib.dump(model, filepath)


def load_model(filepath):
    return joblib.load(filepath)