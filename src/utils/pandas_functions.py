import pandas as pd


def multiplier(df: pd.DataFrame, new_column_name: str, column_target: str, multiplier: int = 1) -> pd.DataFrame:
    df[new_column_name] = df[column_target].apply(lambda x: x * multiplier)
    return df

def rename_columns(df: pd.DataFrame, old_column: str, new_column: str) -> pd.DataFrame:
    df = df.rename(columns={old_column: new_column})
    return df

def add_column(df: pd.DataFrame, column_name: str, value) -> pd.DataFrame:
    df[column_name] = value
    return df
