from prefect import flow, task
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

@task
def data_generation(n_samples: int = 100) -> pd.DataFrame:
    """Generate synthetic dataset"""
    print(f"Generating {n_samples} samples of synthetic data...")
    x = np.random.uniform(-10, 10, n_samples)
    y = 2.5 * x + np.random.normal(0, 2, n_samples)
    df = pd.DataFrame({"feature": x, "target": y})
    print(f"Generated data shape: {df.shape}")
    return df

@task
def data_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the dataset: handle missing values, scale features"""
    print("Preprocessing data...")
    # Drop any missing values
    df_clean = df.dropna().copy()
    # Scale the feature column using StandardScaler
    scaler = StandardScaler()
    df_clean["feature_scaled"] = scaler.fit_transform(df_clean[["feature"]])
    print(f"Preprocessed data shape: {df_clean.shape}")
    print(f"Feature scaled - mean: {df_clean['feature_scaled'].mean():.4f}, "
          f"std: {df_clean['feature_scaled'].std():.4f}")
    return df_clean

@task
def data_loading(df: pd.DataFrame, output_path: str = "processed_data.csv") -> str:
    """Load (save) the processed dataset to a CSV file"""
    print(f"Saving processed data to {output_path}...")
    df.to_csv(output_path, index=False)
    abs_path = os.path.abspath(output_path)
    print(f"Data successfully saved to {abs_path}")
    print(f"Saved columns: {list(df.columns)}")
    return abs_path

@flow
def ml_data_pipeline(n_samples: int = 100, output_path: str = "processed_data.csv") -> str:
    """Data generation -> preprocessing -> loading pipeline"""
    print("=" * 50)
    print("Starting ML Data Pipeline")
    print("=" * 50)

    # Step 1: Generate data
    raw_data = data_generation(n_samples)

    # Step 2: Preprocess data
    processed_data = data_preprocessing(raw_data)

    # Step 3: Load data
    saved_path = data_loading(processed_data, output_path)

    print("=" * 50)
    print("Pipeline completed successfully!")
    print("=" * 50)
    return saved_path

if __name__ == "__main__":
    ml_data_pipeline(n_samples=100, output_path="processed_data.csv")