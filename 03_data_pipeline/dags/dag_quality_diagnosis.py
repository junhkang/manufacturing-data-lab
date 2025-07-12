from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
from datetime import timedelta

from scripts.check_input_files import check_input_files
from scripts.fetch_latest_quality_rules import fetch_latest_quality_rules
from scripts.preprocessing import run_preprocessing
from scripts.labeling import run_labeling
from scripts.generate_report import generate_report
from scripts.notify_slack import notify_if_ng_detected

# 기본 설정
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG 정의
with DAG(
    dag_id='dag_quality_diagnosis',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False,
    description='제조 데이터 품질 진단 파이프라인',
    tags=['quality', 'diagnosis']
) as dag:
    @task()
    def t1_check():
        check_input_files()

    @task()
    def t2_fetch():
        fetch_latest_quality_rules()

    @task()
    def t3_preprocess():
        run_preprocessing()

    @task()
    def t4_label():
        run_labeling()

    @task()
    def t5_report():
        generate_report()

    @task()
    def t6_notify():
        notify_if_ng_detected()

    t1 = t1_check()
    t2 = t2_fetch()
    t3 = t3_preprocess()
    t4 = t4_label()
    t5 = t5_report()
    t6 = t6_notify()


    t1 >> t2 >> t3 >> t4 >> t5 >> t6 


