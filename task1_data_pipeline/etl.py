"""
Task 1 – Data Pipeline
Cleans raw data, encodes categorical columns, scales numeric columns,
and saves the processed data + preprocessor.
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib, os, argparse

RAW_PATH = "titanic_raw.csv"
OUT_DIR = "data/processed"

def load_data(path):
    print(f"Loading data from {path} …")
    return pd.read_csv(path)

def build_preprocessor(df):
    num_cols = df.select_dtypes(include=["int64","float64"]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object","category"]).columns.tolist()

    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler",  StandardScaler())
    ])

    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipe, num_cols),
        ("cat", cat_pipe, cat_cols)
    ])

    return preprocessor, num_cols, cat_cols

def run_etl(input_csv=RAW_PATH, out_dir=OUT_DIR):
    os.makedirs(out_dir, exist_ok=True)
    df = load_data(input_csv)
    df = df.drop_duplicates().reset_index(drop=True)
    print("Initial rows:", len(df))

    preprocessor, num_cols, cat_cols = build_preprocessor(df)
    transformed = preprocessor.fit_transform(df)
    print("Transformed shape:", transformed.shape)

    joblib.dump(preprocessor, os.path.join(out_dir, "preprocessor.joblib"))
    np.save(os.path.join(out_dir, "processed.npy"), transformed)
    print(f"Saved preprocessor + processed data to {out_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=RAW_PATH)
    parser.add_argument("--out",   default=OUT_DIR)
    args = parser.parse_args()
    run_etl(args.input, args.out)