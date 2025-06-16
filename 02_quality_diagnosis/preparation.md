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
│   ├── 04_modeling_svm.ipynb
│   ├── 05_evaluation.ipynb
├── quality_check.ipynb  # 종합용 or 통합 실행

```

---

## 💻 실습 환경

- Python 3.9 이상
- 주피터 노트북(Jupyter Notebook)

### 필수 패키지 목록

```bash
pip install numpy pandas matplotlib opencv-python scikit-learn scikit-image
```

또는 `requirements.txt`로 구성할 경우:

`numpy pandas matplotlib opencv-python scikit-learn scikit-image`

## ▶️ 실행 방법

1. 폴더 위치로 이동
    
2. Jupyter Notebook 실행
    ```bash
cd 02_quality_diagnosis/ jupyter notebook quality_check.ipynb
```
---

## 📌 주의사항 및 참고

- `left_data.csv` 및 `right_data.csv`는 1차 또는 2차 가공된 열화상 데이터입니다.
    
- `left_label.json` 및 `right_label.json`은 수기 라벨 데이터를 기반으로 한 두께(mm) 정보 또는 불량/양품 판단 정보입니다.
    
- 품질 기준:
    - **양품**: `0.8mm < 두께 < 1.5mm`
    - **불량**: `두께 ≤ 0.8mm` 또는 `≥ 1.5mm`