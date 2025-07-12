# 🔧 분석 환경 준비 가이드

실습을 위해 필요한 폴더 구조, 패키지 설치 방법, 실행 방식 등을 안내합니다.

---

## 📁 디렉토리 구조 예시

```
02_quality_diagnosis/
├── raw_data/
│   ├── left_data.csv
│   ├── right_data.csv
├── labels/
│   ├── left_label.json
├── notebooks/
│   ├── 01_visualization.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_labeling.ipynb
│   ├── 04_quality_check.ipynb
│   ├── 05_evaluation.ipynb
```

---

## 💻 실습 환경

- Python 3.9 이상
    
- Jupyter Notebook (주피터 노트북)

## 데이터 출처

https://www.kamp-ai.kr/aidataDetail?AI_SEARCH=&page=1&DATASET_SEQ=6&DISPLAY_MODE_SEL=CARD&EQUIP_SEL=&GUBUN_SEL=&FILE_TYPE_SEL=&WDATE_SEL=

💡 처음 Jupyter 환경을 사용하는 경우 아래 명령어로 설치하세요:

```bash
pip install notebook
```

### 필수 패키지 목록

```bash
pip install numpy pandas matplotlib opencv-python scikit-learn scikit-image
```

또는 `requirements.txt`로 구성할 경우:

```
numpy
pandas
matplotlib
opencv-python
scikit-learn
scikit-image
```

---

## ▶️ 실행 방법

1. 실습 폴더로 이동
    

```bash
cd 02_quality_diagnosis/
```

2. Jupyter Notebook 실행
    

```bash
jupyter notebook quality_check.ipynb
```

---

## 📌 주의사항 및 참고

- `left_data.csv` 및 `right_data.csv`는 1차 또는 2차 가공된 열화상 기반 센서 측정값입니다.
    
- `left_label.json` 및 `right_label.json`은 수기 라벨 데이터를 기반으로 한 두께(mm) 정보입니다.
    
- 기준 범위는 다음과 같습니다:
    
    - **양품**: `0.8mm < 두께 < 1.5mm`
        
    - **불량**: `두께 ≤ 0.8mm` 또는 `≥ 1.5mm`
        
- 두께 기준은 KAMP 머신비전 데이터셋 설명서를 기반으로 설정되었습니다.
    

---

모든 실습은 `quality_check.ipynb` 또는 각 단계별 노트북을 통해 실행할 수 있으며, 분석 결과는 시각화 및 요약 리포트로 확인 가능합니다.