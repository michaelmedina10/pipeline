import json
import yaml


def read_yaml(path:str = 'instructions/instructions.yaml'):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data


def read_json(path: str):
    with open(path, 'r') as f:
        data = json.load(f)
    return data
