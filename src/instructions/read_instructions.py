import json
import yaml
import utils.pandas_functions
from utils.logger import logger

class Instructions:

    def __init__(self, path: str = 'instructions/instructions.yaml'):
        self._path = path
        self._instructions: dict = {}
        self._set_instructions()

    def _set_instructions(self) -> None:
        self._load_instructions()
        self._bind_functions()

    def _load_instructions(self) -> None:
        logger.debug(f'Carregando arquivo - path: {self._path}')
        self._instructions = read_yaml(self._path)

    def get_instructions(self) -> dict:
        return self._instructions

    def _bind_functions(self) -> None:
        for _value in self._instructions.values():
            for _function in _value['pipeline']:
                _function.update({'function': getattr(utils.pandas_functions, _function['function'])})


def read_yaml(path: str):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data

def read_json(path: str):
    with open(path, 'r') as f:
        data = json.load(f)
    return data
