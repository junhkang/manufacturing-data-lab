import os
import logging

def check_input_files():
    required_files = [
        "/opt/airflow/data/left_data.csv",
        "/opt/airflow/data/left_label.json"
    ]

    for data_path in required_files:
        logging.info(f"[check_input_files] Checking file: {data_path}")
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Missing data file: {data_path}")
