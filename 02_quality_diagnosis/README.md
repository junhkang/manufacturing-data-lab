# 프로젝트 2: 열화상 기반 데이터 품질 진단 및 불량 판별 실습

본 실습은 KAMP에서 제공하는 머신비전 AI 데이터셋을 활용하여, 열화상 센서 기반 제품 데이터를 분석하고, 기준 기반 품질 진단을 자동화하는 과정을 학습합니다.

시나리오 및 사전 준비 사항은 아래 문서를 참고하세요:

- [실습 시나리오 보기](https://chatgpt.com/g/g-p-67e67078fd28819181f3d68b5f6c0085-hanhwasiseutemjejogangyi/scenario.md)
    
- [분석 환경 준비 가이드](https://chatgpt.com/g/g-p-67e67078fd28819181f3d68b5f6c0085-hanhwasiseutemjejogangyi/preparation.md)
    

---

## 🎯 실습 목표

- 열화상 기반 온도 벡터 데이터를 로딩 및 구조 이해
    
- 제품별 두께 정보를 기준으로 OK/NG 자동 분류
    
- 온도 벡터와 품질 기준을 결합한 진단 및 리포트 생성
    

---

## 📁 데이터 구조

- `left_data.csv`: 각 행은 제품 1개의 열화상 온도 벡터 데이터 (1D 벡터)
    
- `left_label.json`: 각 제품 ID에 해당하는 두께 정보 (수기 기록, 단위 mm)
    
- ※ 기준값: `0.8mm < 두께 < 1.5mm` → **양품**, 이외는 **불량**으로 간주
    

---

## 🧪 실습 단계

1. **데이터 로딩 및 확인**
    
    - `left_data.csv`, `left_label.json` 불러오기 및 병합
        
2. **두께 기준 기반 라벨 생성**
    
    - `OK` / `NG` 자동 태깅
        
3. **온도 벡터 시각화**
    
    - 샘플 1D 벡터를 `plot()` 또는 이미지로 시각화
        
4. **품질 분포 요약**
    
    - 전체 OK/NG 비율 및 통계 계산, 라벨 분포 시각화
        
5. **진단 결과 저장**
    
    - 최종 결과를 CSV로 저장
        

---

## 🔧 분석 환경

- Python 3.9 이상
    
- 주요 라이브러리:  
    `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `scikit-image`, `opencv-python`, `json`
    

---

## 📦 실행 방식

- 실습은 `quality_check.ipynb` 또는 다음의 단계별 노트북을 통해 진행
    
    - `01_visualization.ipynb`: 데이터 시각화
        
    - `02_preprocessing.ipynb`: ROI 추출, 정규화
        
    - `03_labeling.ipynb`: 기준 기반 라벨 생성
        
    - `04_quality_check.ipynb`: 전체 품질 진단
        
    - `05_evaluation.ipynb`: 요약 및 시각화
        

---

## 📌 주의사항

- `left_label.json` 내 두께 기준은 KAMP 공식 가이드라인을 바탕으로 설정됨
    
- 본 실습은 머신러닝 예측이 아닌, **기준 기반의 자동 품질 진단 프로세스 설계**에 초점을 둠