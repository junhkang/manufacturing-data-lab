import pandas as pd
import logging
import os

def generate_report():
    input_path = "/opt/airflow/data/labeled_data.csv"
    report_path = "/opt/airflow/data/report.txt"


    df = pd.read_csv(input_path)
    counts = df["label"].value_counts()
    with open(report_path, "w") as f:
        f.write("Quality Diagnosis Report\n")
        f.write("======================\n")
        for label, count in counts.items():
            f.write(f"{label}: {count} items\n")

    logging.info(f"[generate_report] Report written to {report_path}")



