# 🛠️ 제조 품질 진단 데이터 파이프라인 자동화 실습

본 실습은 Airflow를 활용하여 제조 현장의 품질 진단 과정을 자동화하는 데이터 파이프라인을 구현합니다.  
센서 기반 고차원 벡터 데이터를 활용하여 전처리, 이상치 탐지, 라벨링, 평가 및 리포트까지의 과정을 DAG(Task 흐름)으로 자동화합니다.

---

## 📁 디렉토리 구조

<pre><code>quality_diagnosis_pipeline/
├── dags/
│   └── dag_quality_diagnosis.py      # 실습의 핵심 DAG 정의
├── scripts/
│   ├── preprocessing.py              # 전처리 및 정규화 로직
│   ├── evaluation.py                 # 평가 및 통계 리포트 생성
│   └── upload_to_s3.py               # 결과 S3 업로드 (또는 로컬 저장)
├── data/
│   ├── left_data.csv                 # 열화상 센서 기반 벡터 데이터
│   ├── left_label.json               # 두께 라벨 데이터
│   └── quality_rules/                # 기준 버전별 JSON (자동 선택)
├── logs/                             # Airflow 실행 로그 디렉토리
├── output/                           # 결과 리포트 및 시각화 저장
├── scenario.md                       # 실습 시나리오 설명서
├── preparation.md                    # 사전 준비 환경 구성 가이드
└── README.md                         # 본 파일
</code></pre>

---

## ⚙️ 환경 요구 사항

- Python 3.9 이상
- Airflow 2.7.x 이상
- pandas, numpy, matplotlib
- (선택) boto3 (S3 업로드용)
- (선택) SlackWebhookOperator를 위한 Slack API Token

Airflow는 **Docker 기반 또는 로컬 환경**에서 구동 가능합니다. 자세한 설정은 `preparation.md`를 참고하세요.

---

## 🚀 실행 방법

1. **Airflow 환경 구성**
   - `preparation.md` 참고하여 Airflow 설치 및 dags 디렉토리 등록

2. **DAG 활성화**
   - Airflow Web UI 접속 후 `dag_quality_diagnosis` DAG 활성화 (`ON`)

3. **DAG 수동 실행 또는 일정 기반 트리거**
   - 예: 매일 오전 5시 실행되도록 설정 (`schedule_interval="0 5 * * *"`)

4. **Task 로그 확인**
   - 각 Task 별 로그를 통해 처리 현황 및 결과 확인 가능

---

## 📦 주요 Task 요약

| Task 이름 | 설명 |
|-----------|------|
| `check_input_files` | 데이터 및 기준 파일 존재 여부 확인 |
| `fetch_latest_quality_rules` | 가장 최신 품질 기준 파일 자동 선택 |
| `load_data_files` | CSV 및 JSON 파일 로드 |
| `preprocess_roi` | 중심 영역(ROI) 추출 |
| `normalize_vector` | 정규화 수행 |
| `detect_outliers` | 벡터 기반 이상치 탐지 |
| `label_data` | 라벨링 (등급 + OK/NG 조합) |
| `evaluate_results` | 통과율 계산 및 경계 샘플 분석 |
| `generate_report` | 시각화 리포트 및 .csv 생성 |
| `upload_report_to_s3` | 결과 저장 (S3 또는 로컬) |
| `slack_notify_if_needed` | 조건 만족 시 Slack 알림 전송 (선택적 구현) |

---

## 📈 결과 예시

- `/output/report_YYYYMMDD.csv`: 하루치 품질 진단 결과
- `/output/visual_YYYYMMDD.png`: 등급별 샘플 분포 시각화
- Slack 메시지 (예시):  
  `"⚠️ NG 비율이 15%를 초과했습니다. 공정 점검 필요"`

---

## 📌 참고 문서

- [scenario.md](./scenario.md): 전체 실습 배경과 목적 설명
- [preparation.md](./preparation.md): 실습 환경 설치 가이드
- [Airflow 공식 문서](https://airflow.apache.org/docs/): 오케스트레이션 이해용

---

> 본 실습은 실제 제조 현장의 품질 진단 흐름을 모델링한 예제로,  
> 단순한 ETL을 넘어 복잡한 조건 분기와 반복 실행 구조를 이해하는 데 중점을 둡니다.
