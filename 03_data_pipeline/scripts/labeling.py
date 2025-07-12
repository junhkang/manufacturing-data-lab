import pandas as pd
import json
import logging
import os
from pathlib import Path

def run_labeling():
    label_path = "/opt/airflow/data/left_label.json"
    output_path = "/opt/airflow/data/labeled_data.csv"

    with open(label_path, "r") as f:
        label_list = json.load(f)

    df = pd.DataFrame({"thickness": label_list})

    def classify(th):
        return "OK" if 0.8 <= th <= 1.5 else "NG"

    df["label"] = df["thickness"].apply(classify)


    df.to_csv(output_path, index=False)

    logging.info(f"[labeling] Saved labeled data to {output_path}")




