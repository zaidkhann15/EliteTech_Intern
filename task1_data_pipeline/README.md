# Task 1 – Data Pipeline Development

## Goal
Clean and preprocess raw data (Titanic dataset), encode categorical columns,
scale numerical columns, and save the processed outputs.

## Steps to Run
1. Activate virtual env and install requirements  
2. Ensure `titanic_raw.csv` exists in this folder  
3. Run:
   python etl.py --input titanic_raw.csv --out data/processed

Outputs:
- `data/processed/processed.npy`  
- `data/processed/preprocessor.joblib`

## Files
- `etl.py` – main pipeline script  
- `notebook.ipynb` – exploration & visualization  
- `requirements.txt` – dependencies  
- `README.md` – instructions


Developed By:
Zaid Khan
EliteTech Internship – Task 3: Data Pipeline Development