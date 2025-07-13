# 🧬 제조 품질 진단 데이터 파이프라인 자동화 실습 (with AWS Glue)

본 실습은 **AWS Glue**를 활용하여 제조 품질 진단 프로세스를 클라우드 기반 데이터 파이프라인으로 구현합니다.  
Glue의 크롤링, 변환, 정제 기능을 활용해 **센서 기반 품질 벡터 데이터를 전처리, 라벨링, 통계 분석 후 Athena에서 쿼리 가능한 상태로 저장**하는 전 과정을 실습합니다.

---
## 📁 디렉토리 구조

```
glue_quality_diagnosis/
├── scripts/
│   ├── glue_job_preprocessing.py     # 벡터 정규화 및 ROI 추출
│   ├── glue_job_labeling.py          # 라벨 생성 및 품질 진단
│   ├── glue_job_evaluation.py        # 통계 분석 및 시각화 (선택)
│   └── glue_job_upload.py            # 결과 저장 (S3 + Parquet)
├── crawler/
│   └── glue_crawler_config.json      # Glue 크롤러 설정 파일
├── catalog/
│   └── create_table.sql              # Athena 테이블 생성 쿼리
├── data/
│   ├── raw/                          # 원본 CSV, JSON (S3에 업로드됨)
│   └── processed/                    # 결과 저장 (Parquet + Report)
├── scenario.md                       # 실습 시나리오 설명서
├── preparation.md                    # 사전 준비 환경 구성 가이드
└── README.md                         # 본 개요 파일
```

---

## ⚙️ 환경 요구 사항

- AWS 계정 (필수)
- IAM 권한: Glue, S3, Athena, CloudWatch Logs, LakeFormation
- Glue Studio 또는 Script 모드 지원
- S3 Bucket 사전 생성 필요 (예: `s3://glue-quality-lab`)
- (선택) Athena Workgroup 구성
- (선택) CloudTrail, CostExplorer 권장 (운영 추적)

---

## 🎯 실습 목표

- AWS Glue를 활용한 **데이터 전처리 자동화**
- S3 기반의 원본/가공 데이터 저장 구조 설계
- 크롤러를 활용한 **동적 스키마 추론**
- 결과 데이터를 Athena에서 **즉시 SQL 쿼리 가능한 상태로 저장**
- 운영 환경에서 활용 가능한 **클라우드 네이티브 품질 진단 파이프라인 구축**

---

## 🧪 주요 Step

| 단계 | 설명 |
|------|------|
| Step 1 | 원본 CSV 및 라벨 JSON을 S3에 업로드 |
| Step 2 | Glue Crawler를 통해 S3 구조 및 스키마 추론 |
| Step 3 | Glue Job 1 - 데이터 정규화 및 ROI 추출 |
| Step 4 | Glue Job 2 - 기준 기반 라벨링 및 NG 판정 |
| Step 5 | Glue Job 3 - 통계 분석 및 NG 비율 산출 |
| Step 6 | Parquet 저장 및 결과 경로에 테이블 생성 |
| Step 7 | Athena에서 품질 쿼리 및 조건부 분석 수행 |

---

## ✅ 실습 결과물 예시

- `s3://glue-quality-lab/processed/report_20250712.parquet`
- Athena Table: `quality_diagnosis_result`
- 시각화 도구 연계(선택): Amazon QuickSight 또는 외부 BI

---

## 📌 참고 문서

- [scenario.md](./scenario.md): 실습 배경과 문제 상황 설명
- [preparation.md](./preparation.md): AWS 자원 준비 및 Glue 설정 가이드
- [AWS Glue 공식 문서](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Athena 공식 문서](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

---

> 본 실습은 **"Athena에서 즉시 분석 가능한 제조 품질 데이터를 Glue로 어떻게 자동화할 것인가?"를 중심 주제로 구성되었습니다.  
> 기존 로컬 기반 ETL의 한계를 넘어서기 위한 실무 기반 클라우드 전환 예제로,  
> Glue의 Job 관리, Crawler, S3-Partition 설계 및 Athena 연계 전략을 실습 중심으로 학습합니다.
