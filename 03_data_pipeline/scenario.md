# 📘 Scenario: 제조 품질 진단 데이터 파이프라인 자동화

## 🎯 실습 목적

본 실습은 제조 현장에서 수집된 열화상 센서 기반 고차원 데이터와 품질 기준 라벨을 활용하여  
**Airflow 기반의 데이터 파이프라인 자동화 프로세스를 설계**하고 실행하는 것을 목표로 합니다.

기존에는 수작업으로 처리되던 품질 진단 프로세스를,  
Airflow를 활용해 자동화된 **DAG(Directed Acyclic Graph)** 구조로 전환하며  
현업에서 활용 가능한 데이터 오케스트레이션 실무 감각을 기릅니다.

---

## 🏭 업무 시나리오

A 제조기업에서는 제품 생산 과정에서 센서 데이터를 지속적으로 수집하고 있으며,  
해당 데이터는 매일 새벽 4시에 S3에 저장됩니다.

데이터 분석팀은 아래와 같은 주기적인 작업을 수행하고 있습니다:

- 열화상 센서 기반 벡터 데이터의 전처리 및 정규화
- 최신 품질 기준에 따른 등급 라벨링 및 OK/NG 판단
- 일일 품질 리포트 생성 및 S3 업로드
- 기준 이상으로 NG 비율이 높을 경우 Slack을 통한 알림 발송 (선택)

이제 이 과정을 **Airflow DAG으로 자동화**하여 운영 효율성을 개선하려고 합니다.

---

## 🛠️ 실습에서 구현할 파이프라인 개요

- S3 또는 로컬에서 벡터 데이터(`left_data.csv`) 및 라벨(`left_label.json`) 불러오기
- 기준 파일(`quality_rules.json`)은 가장 최근 수정된 버전 자동 선택
- 중심 ROI 추출 및 Min-Max 정규화
- 이상치 탐지 및 라벨 생성 (등급화 및 OK/NG 조합)
- 품질 통과율, 경계값 분석, 시각화 리포트 생성
- 리포트를 S3에 업로드
- NG 비율이 일정 기준을 초과할 경우 Slack 알림 (옵션, 구현 생략)

---

## 📊 데이터 요약

| 파일명                  | 설명                            |
| -------------------- | ----------------------------- |
| `left_data.csv`      | 제품 1개당 약 80,000차원의 고차원 센서 벡터  |
| `left_label.json`    | 제품의 실제 두께 라벨 정보 (품질 판단 기준)    |
| `quality_rules.json` | 기준별 품질 조건 및 등급 라벨링 기준, 버전별 존재 |

---

## 📈 Airflow DAG 흐름 요약

```text
check_input_files
 └── fetch_latest_quality_rules
       └── load_data_files
             └── preprocess_roi
                   ├── normalize_vector
                   └── detect_outliers
                         └── label_data
                               ├── evaluate_results
                               ├── generate_report
                               │     └── upload_report_to_s3
                               └── check_quality_alert_threshold
                                     └── slack_notify_if_needed
```

---

## ✅ 실습 학습 목표

- Airflow DAG 작성법과 구성요소 (Task, Operator, Schedule 등) 이해
- 현실적인 데이터 흐름을 기반으로 한 DAG 구성 연습
- Task 간 의존성과 분기(Branch) 처리 구조 학습
- 단순한 ETL을 넘어서 **조건 기반 알림 및 리포팅까지 확장**된 자동화 실습 경험

---

## 🔚 실습 완료 후 기대 결과

- Airflow UI에서 DAG가 자동 실행되고, 각 Task의 상태를 시각적으로 확인
- `.csv` 형식의 품질 진단 리포트가 S3 (또는 로컬 폴더)에 저장됨
- 알림 조건을 만족하면 Slack으로 메시지 전송 (단, 본 실습에선 가능 여부만 설명)

