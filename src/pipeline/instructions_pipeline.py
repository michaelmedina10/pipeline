import pandas as pd

from instructions.read_instructions import read_json

def transform_to_pandas(path: str = 'data_source/pessoas.json'):
    df = pd.DataFrame(read_json(path))
    return df
