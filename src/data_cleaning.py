"""
Task: 1 -  Data Cleaning and Preprocessing
File: data_cleaning.py
Author: Kamsala Venkata Sai Vinay
Description: Cleans and preprocesses the Customer Personality Analysis dataset.
"""

import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Dataset loaded successfully with shape {df.shape}")
        return df
    except FileNotFoundError:
        logging.error("File not found. Check the file path.")
        raise
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        raise

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in the dataset.
    Fill numeric columns with median, categorical with 'Unknown'.
    """
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                df[col].fillna('Unknown', inplace=True)
            else:
                df[col].fillna(df[col].median(), inplace=True)
            logging.info(f"Filled missing values in column: {col}")
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the dataset.
    """
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    logging.info(f"Removed {before - after} duplicate rows.")
    return df

def standardize_text(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize text columns for consistency.
    """
    if 'Education' in df.columns:
        df['Education'] = df['Education'].str.lower().str.strip()
        df['Education'].replace({'2n cycle': 'second_cycle'}, inplace=True)
    if 'Marital_Status' in df.columns:
        df['Marital_Status'] = df['Marital_Status'].str.lower().str.strip()
        df['Marital_Status'].replace({'together': 'married'}, inplace=True)
    logging.info("Standardized text columns.")
    return df

def convert_date_columns(df: pd.DataFrame, date_cols: list) -> pd.DataFrame:
    """
    Convert specified columns to datetime format.
    """
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            logging.info(f"Converted column '{col}' to datetime.")
    return df

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns to lowercase with underscores.
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    logging.info("Renamed columns for consistency.")
    return df

def add_age_column(df: pd.DataFrame, birth_col: str) -> pd.DataFrame:
    """
    Add 'age' column based on birth year.
    """
    if birth_col in df.columns:
        df['age'] = datetime.now().year - df[birth_col]
        logging.info("Added 'age' column.")
    return df

def save_dataset(df: pd.DataFrame, output_path: str):
    """
    Save cleaned dataset to CSV.
    """
    df.to_csv(output_path, index=False)
    logging.info(f"Cleaned dataset saved to {output_path}")

def main():
    # File paths
    input_file = 'E:\ELEVATE LABS\Task 1 -  Data Cleaning and Preprocessing\datasets\marketing_campaign.csv'
    output_file = 'cleaned_marketing_campaign.csv'

    # Load dataset
    df = load_dataset(input_file)

    # Cleaning steps
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = standardize_text(df)
    df = convert_date_columns(df, ['Dt_Customer'])
    df = rename_columns(df)
    df = add_age_column(df, 'year_birth')

    # Save cleaned dataset
    save_dataset(df, output_file)

    # Summary
    logging.info(f"Final dataset shape: {df.shape}")

if __name__ == "__main__":
    main()
