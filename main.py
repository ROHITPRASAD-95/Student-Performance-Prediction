import os
from src.utils import create_directories


def run_pipeline():
    create_directories()

    os.system('python src/generate_data.py')
    os.system('python src/preprocess.py')
    os.system('python src/train.py')
    os.system('python src/evaluate.py')

    print('\nProject executed successfully!')


if __name__ == '__main__':
    run_pipeline()