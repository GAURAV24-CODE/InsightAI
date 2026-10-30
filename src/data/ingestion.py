from pathlib import Path

import pandas as pd


def load_data(file_path: Path) -> pd.DataFrame:
    """
    Load the Superstore dataset into a pandas DataFrame.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    if file_path.suffix.lower() == ".xls":
        df = pd.read_excel(file_path, engine="xlrd")

    elif file_path.suffix.lower() == ".xlsx":
        df = pd.read_excel(file_path)

    elif file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Use CSV, XLS, or XLSX."
        )

    return df