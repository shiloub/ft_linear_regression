import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a csv file and return a pandas-dataframe"""
    try:
        assert path.endswith(".csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except (FileNotFoundError, AssertionError, PermissionError):
        print("Error loading the file")
        return None
