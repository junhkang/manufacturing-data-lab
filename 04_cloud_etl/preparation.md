# 🔧 AWS Glue 실습 사전 준비 가이드 (`preparation.md`)

본 실습에서는 AWS Glue, S3, Glue Crawler, 그리고 Athena를 활용해 제조 품질 진단 데이터를 자동 처리하고 분석 가능한 형태로 구성합니다.  
아래 항목들을 순서대로 준비해 주세요.

---

## ✅ 사전 요구사항

- AWS 계정 (관리자 권한 또는 해당 서비스 접근 권한 필요)
- Glue, S3, Athena, IAM, CloudWatch 등의 사용 가능 Region에서 진행
- Athena 및 Glue Studio 기본 사용법에 대한 이해

---

## 🪣 1. S3 버킷 준비

1. `glue-quality-lab` 와 같은 이름으로 S3 버킷 생성
2. 아래 폴더 구조로 디렉토리 구성:

```plaintext
s3://your-bucket-name/
├── input/
│   ├── left_data.csv
│   └── left_label.json
├── output/
│   ├── report_20250701.csv
│   └── visualization_20250701.png
└── quality_rules/
    ├── rule_v1.0.json
    └── rule_v2.0.json
```


3. 로컬에서 제공된 `left_data.csv`, `left_label.json`을 `/raw/` 경로에 업로드

---

## 🔐 2. IAM Role 설정 (Glue용)

1. IAM 콘솔 → 역할(Role) → 새 역할 생성
2. 신뢰 관계: **Glue** 서비스
3. 권한 정책:
   - `AmazonS3FullAccess`
   - `AWSGlueServiceRole`
   - `AmazonAthenaFullAccess`
   - (선택) `CloudWatchLogsFullAccess`
4. 이름 예시: `AWSGlueQualityLabRole`

---

## 🧪 3. AWS Glue Crawler 구성

1. Glue 콘솔 → **Crawler 생성**
2. 데이터 위치: `s3://glue-quality-lab/raw/`
3. IAM 역할: `AWSGlueQualityLabRole`
4. 출력 DB: `quality_lab_db` (신규 생성 가능)
5. 테이블명 예시: `sensor_raw_data`

> Crawler 실행 후, Athena에서 `SELECT * FROM quality_lab_db.sensor_raw_data`로 조회 가능

---

## 💻 4. Glue Job 환경 준비

1. Glue Studio → 새 Job 생성
2. **Python Shell 또는 Spark** 기반 Job 선택
3. 스크립트 경로: `/scripts/glue_job_preprocessing.py` 등
4. Script Parameters:
   - 입력 S3: `s3://glue-quality-lab/raw/`
   - 출력 S3: `s3://glue-quality-lab/processed/`
5. IAM Role: `AWSGlueQualityLabRole`
6. Glue Version: **3.0 이상**, Python **3.9** 권장
7. 추가 Python 라이브러리 필요 시:
   - `pandas`, `numpy` 등은 Glue 내장
   - `matplotlib` 등은 별도 wheel 패키지 업로드 필요

---

## 📊 5. Athena 설정 (결과 쿼리용)

1. Glue Job 완료 후 `/processed/` 경로에 Parquet 파일 생성됨
2. Glue Crawler를 `/processed/` 대상으로 추가 구성
3. Athena에서 쿼리 확인:
   ```sql
   SELECT * FROM quality_lab_db.processed_results
```

## 🔔 6. (선택) 알림 설정

- Slack 또는 이메일 알림을 설정하고 싶은 경우 CloudWatch Logs 또는 Lambda + SNS 연동 필요
- 본 실습에서는 기본적으로 `CloudWatch Logs` 확인

---

## 🧷 참고사항

- 실습 스크립트는 `scripts/` 디렉토리에 있습니다.
- 환경 비용 최소화를 위해 사용 종료 후 리소스 정리 권장:
    - Glue Job/DB/Table/Crawler 삭제
    - S3 버킷 비우기 또는 제거
    - IAM 역할 확인
