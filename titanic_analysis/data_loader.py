import pandas as pd
def load_titanic_data(filepath: str) -> pd.DataFrame:
    data = pd.read_csv(filepath)
    return data
