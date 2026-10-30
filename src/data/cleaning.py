import pandas as pd


def clean_column_names(df):
    """Remove unnecessary spaces from column names."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    return df


def clean_text_columns(df):
    """Clean whitespace from text columns."""
    df = df.copy()

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    return df


def clean_date_and_numeric_columns(df):
    """Clean date and numeric columns."""
    df = df.copy()

    date_columns = ["Order Date", "Ship Date"]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    numeric_columns = [
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def handle_missing_values(df):
    """Handle missing values in critical analytical columns."""
    df = df.copy()

    critical_columns = [
        "Order Date",
        "Ship Date",
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    df = df.dropna(subset=critical_columns)

    return df


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    df = df.copy()

    before = len(df)

    df = df.drop_duplicates()

    removed = before - len(df)

    print(f"Duplicate rows removed: {removed}")

    return df


def clean_postal_code(df):
    """Treat Postal Code as an identifier."""
    df = df.copy()

    df["Postal Code"] = df["Postal Code"].astype("string")

    return df


def final_quality_check(df):
    """Validate the quality of the cleaned dataset."""

    critical_columns = [
        "Order Date",
        "Ship Date",
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    missing_critical = df[critical_columns].isna().sum().sum()
    duplicate_rows = df.duplicated().sum()

    if missing_critical > 0:
        raise ValueError(
            f"Final quality check failed: "
            f"{missing_critical} missing values in critical columns."
        )

    if duplicate_rows > 0:
        raise ValueError(
            f"Final quality check failed: "
            f"{duplicate_rows} duplicate rows found."
        )

    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Missing values in critical columns:", missing_critical)
    print("Duplicate rows:", duplicate_rows)

    optional_missing = df.isna().sum()
    optional_missing = optional_missing[optional_missing > 0]

    if not optional_missing.empty:
        print("\nOptional missing values:")
        print(optional_missing)

    print("\n✅ Final data quality check passed!")

    return True