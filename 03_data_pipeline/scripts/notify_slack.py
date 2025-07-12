import pandas as pd
import logging
import os

def notify_if_ng_detected():
    report_path = "/opt/airflow/data/report.txt"

    with open(report_path, "r") as f:
        content = f.read()
        if "NG" in content:
            logging.info("[notify_slack] NG detected")
        else:
            logging.info("[notify_slack] No NG items found.")
