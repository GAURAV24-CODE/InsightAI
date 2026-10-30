REQUIRED_COLUMNS = [
    "Row ID",
    "Order ID",
    "Order Date",
    "Ship Date",
    "Ship Mode",
    "Customer ID",
    "Customer Name",
    "Segment",
    "Country/Region",
    "City",
    "State/Province",
    "Postal Code",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name",
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
]


def validate_required_columns(df):
    """Check whether all required columns exist."""

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return True


def validate_missing_values(df):
    """Check for missing values in the dataset."""

    missing_values = df.isna().sum()
    missing_columns = missing_values[missing_values > 0]

    if not missing_columns.empty:
        raise ValueError(
            f"Missing values found:\n{missing_columns}"
        )

    return True


def validate_duplicates(df):
    """Check for duplicate rows in the dataset."""

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        raise ValueError(
            f"Duplicate rows found: {duplicate_count}"
        )

    return True



import pandas as pd


def validate_data_types(df):
    """Check whether important columns have the expected data types."""

    date_columns = ["Order Date", "Ship Date"]
    numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]

    for column in date_columns:
        if not pd.api.types.is_datetime64_any_dtype(df[column]):
            raise TypeError(
                f"{column} must be a datetime column."
            )

    for column in numeric_columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(
                f"{column} must be a numeric column."
            )

    return True



def validate_business_rules(df):
    """Validate business rules for the Superstore dataset."""

    errors = []

    if (df["Quantity"] <= 0).any():
        errors.append("Quantity must be greater than 0.")

    if (df["Sales"] < 0).any():
        errors.append("Sales cannot be negative.")

    if ((df["Discount"] < 0) | (df["Discount"] > 1)).any():
        errors.append("Discount must be between 0 and 1.")

    if (df["Order Date"] > df["Ship Date"]).any():
        errors.append("Order Date cannot be after Ship Date.")

    if errors:
        raise ValueError(
            "Business rule validation failed:\n"
            + "\n".join(errors)
        )

    return True




def validate_dataset(df):
    """Run all dataset validation checks."""

    validate_required_columns(df)
    validate_missing_values(df)
    validate_duplicates(df)
    validate_data_types(df)
    validate_business_rules(df)

    return True