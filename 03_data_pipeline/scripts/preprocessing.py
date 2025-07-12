import pandas as pd
import logging
import os

def run_preprocessing():
    input_path = "/opt/airflow/data/left_data.csv"
    output_path = "/opt/airflow/data/preprocessed.csv"

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Data file not found: {input_path}")

    logging.info(f"[preprocessing] Loading CSV from {input_path}")
    df = pd.read_csv(input_path, header=None)
    df_roi = df.iloc[:, 100:201]

    logging.info("[preprocessing] Normalizing data (min-max)")
    df_norm = (df_roi - df_roi.min()) / (df_roi.max() - df_roi.min())
    df_norm.to_csv(output_path, index = False)

    logging.info(f"[preprocessing] Saved to {output_path}")

