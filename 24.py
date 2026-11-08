import numpy as np
import pandas as pd


def clean_and_preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:

    # Work on a copy to avoid mutating original data
    cleaned_df = df.copy()

    # --- Step 1: Standardize Column Names ---
    # Convert to lowercase, strip leading/trailing whitespace, replace spaces with underscores
    cleaned_df.columns = (
        cleaned_df.columns.str.strip().str.lower().str.replace(" ", "_")
    )
    print("✓ Column names standardized.")

    # --- Step 2: Handle Duplicate Rows ---
    initial_rows = len(cleaned_df)
    cleaned_df = cleaned_df.drop_duplicates()
    duplicates_removed = initial_rows - len(cleaned_df)
    print(f"✓ Removed {duplicates_removed} duplicate row(s).")

    # --- Step 3: Standardize Text/Categorical Data ---
    # Strip whitespace and convert strings to title case (if text columns exist)
    text_cols = cleaned_df.select_dtypes(include=["object", "string"]).columns
    for col in text_cols:
        cleaned_df[col] = cleaned_df[col].astype(str).str.strip()

    # --- Step 4: Handle Missing Values ---
    # Numerical: Fill missing values with column median
    num_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        if cleaned_df[col].isnull().sum() > 0:
            median_val = cleaned_df[col].median()
            cleaned_df[col] = cleaned_df[col].fillna(median_val)

    # Categorical/Object: Fill missing values with the mode (most frequent)
    for col in text_cols:
        if (
            cleaned_df[col].isnull().sum() > 0
            or (cleaned_df[col] == "nan").sum() > 0
        ):
            # Replace string 'nan' produced during str casting back to actual null
            cleaned_df[col] = cleaned_df[col].replace("nan", np.nan)
            mode_val = cleaned_df[col].mode()[0]
            cleaned_df[col] = cleaned_df[col].fillna(mode_val)

    print("✓ Missing values imputed (Numeric -> Median, Categorical -> Mode).")

    # --- Step 5: Convert Data Types & Parse Dates ---
    # Example: Parse date columns if present (e.g., 'join_date')
    date_cols = [col for col in cleaned_df.columns if "date" in col]
    for col in date_cols:
        cleaned_df[col] = pd.to_datetime(cleaned_df[col], errors="coerce")

    # --- Step 6: Outlier Handling (IQR Capping) ---
    # Cap numerical extreme outliers to 1.5 * IQR bounds to prevent skewed analysis
    for col in num_cols:
        Q1 = cleaned_df[col].quantile(0.25)
        Q3 = cleaned_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        cleaned_df[col] = np.where(
            cleaned_df[col] < lower_bound, lower_bound, cleaned_df[col]
        )
        cleaned_df[col] = np.where(
            cleaned_df[col] > upper_bound, upper_bound, cleaned_df[col]
        )

    print("✓ Outliers capped using IQR thresholding.")

    return cleaned_df


# ==========================================
# Example Usage with Dirty Sample Data
# ==========================================
if __name__ == "__main__":
    # Create a dummy messy dataset
    raw_data = {
        " Customer ID ": [101, 102, 103, 103, 104, 105],  # Trailing space, duplicate 103
        "Name ": [" Alice ", "bob", "Charlie", "Charlie", "David", np.nan],  # Inconsistent casing/spaces, null
        " Age ": [25, np.nan, 35, 35, 120, 29],  # Outlier (120), missing value
        "Salary": [50000, 60000, np.nan, np.nan, 75000, 52000],  # Missing values
        "Join Date": ["2022-01-15", "2021-06-10", "2023-03-01", "2023-03-01", "invalid_date", "2022-11-20"]
    }

    raw_df = pd.DataFrame(raw_data)

    print("--- RAW DATASET ---")
    print(raw_df)
    print("\n" + "=" * 40 + "\n")

    # Run pipeline
    cleaned_df = clean_and_preprocess_dataset(raw_df)

    print("\n--- CLEANED DATASET ---")
    print(cleaned_df)
    print("\n--- DATA TYPES ---")
    print(cleaned_df.dtypes)