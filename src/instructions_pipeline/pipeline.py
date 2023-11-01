import pandas as pd

from instructions.read_instructions import read_json, Instructions
from utils.handle_file import save_pickle


def pipeline() -> dict:

    instructions = pipeline_input()
    data_output = pipeline_output(instructions=instructions)
    save_pickle(data_output)
    return data_output


def pipeline_input() -> dict:
    instructions = Instructions().get_instructions()

    for service in instructions.keys():
        source_path = instructions[service].get('get_data')
        instructions[service]['get_data'] = transform_to_pandas(**source_path)
    return instructions


def pipeline_output(instructions: dict) -> dict:

    dict_output = {}
    for key, value in instructions.items():
        df_base = instructions[key].pop('get_data')
        for pipeline in value.values():
            dict_output[key] = transform_pipeline(df_base, pipeline)
    return dict_output


def transform_to_pandas(path: dict) -> pd.DataFrame:
    df = pd.DataFrame(read_json(path))
    return df


def transform_pipeline(df: pd.DataFrame, instructions_pipeline: list) -> pd.DataFrame:
    for function in instructions_pipeline:
        df = df.pipe(function['function'], **function['params'])
    return df
