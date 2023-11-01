import pickle


def save_pickle(data) -> None:

    with open('data_output.pkl', 'wb') as f:
        pickle.dump(data, f)

def read_pickle() -> dict:

    with open('data_output.pkl', 'rb') as f:
        data = pickle.load(f)
    return data
