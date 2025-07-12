# 실습 환경 구성 가이드

본 문서는 제조 품질 진단 자동화 실습을 위한 Airflow 실행 환경을 구성하는 방법을 안내합니다.  
Docker 기반 설치를 기본으로 하며, 로컬 환경 또는 EC2에서도 동일한 방식으로 구동 가능합니다.

---

## ✅ 사전 요구 사항

- Docker 및 Docker Compose 설치 완료
    
- Python 3.9 이상 (로컬 실행 시)
    
- Git (실습 저장소 clone용)
    

---

## 🚀 1. Airflow Docker 환경 구성 (권장)

### 1-1. 공식 Airflow Docker 예제 clone

```bash
git clone https://github.com/apache/airflow.git
cd airflow
git fetch --all --tags
git checkout tags/2.7.3 -b airflow-2.7.3

OR

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'

```

### 1-2. 기본 설정 초기화

```bash
cp .env.example .env
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" >> .env
```

### 1-3. 실습용 DAG 및 스크립트 연결

```bash
cp -r ~/quality_diagnosis_pipeline/dags/* ./dags/
cp -r ~/quality_diagnosis_pipeline/scripts ./dags/scripts
```

---

### 1-4. Docker Compose로 실행

```bash
docker-compose up -d
```

> 최초 실행 시 Airflow 웹 UI는 [http://localhost:8080](http://localhost:8080/) 에서 접근 가능  
> 기본 계정은 `airflow / airflow` 입니다.

---

## 🛠️ 2. Airflow Web UI 접근 후 DAG 확인

1. [http://localhost:8080](http://localhost:8080/) 접근
    
2. `dag_quality_diagnosis` DAG 활성화 (스위치 ON)
    
3. 수동 실행 버튼 클릭 또는 일정 기본 스케줄리링 설정
    

---

## 🥪 3. 결과 확인 및 디버깅

- DAG 실행 로그 확인: UI 상단의 Logs 탭
    
- 출력 파일 확인: `output/` 포넛더 내 `.csv`, `.png` 파일
    
- Slack 알림: 실제 연동하지 않고도 조건 판단 Task는 정상 실행됨
    

---

## 🐍 (선택) 로컬 가상환경 실행 방법

```bash
python -m venv venv
source venv/bin/activate

pip install apache-airflow==2.7.3 \
  --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.9.txt

export AIRFLOW_HOME=~/airflow
airflow db init

airflow users create \
  --username admin \
  --firstname admin \
  --lastname admin \
  --role Admin \
  --email admin@example.com \
  --password admin

airflow webserver --port 8080
airflow scheduler
```

※ dags 포넛더에 실습용 DAG 복사 필요

---

## 🔗 참고 링크

- [https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)
    
- [https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)
    

---

> 실습이 시작되기 전까지 DAG 파일과 스크립트가 정상적으로 반영되는지 확인해 주세요.  
> 오류 발생 시 각 Task 로그를 먼저 확인하고, DAG 정의 및 Operator 구성을 검토하세요.