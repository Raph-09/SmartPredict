import yaml
import os

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml, 'r') as f:
        return yaml.safe_load(f)


def create_directories(paths: list):
    for path in paths:
        os.makedirs(path, exist_ok=True)
