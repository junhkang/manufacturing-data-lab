# 프로젝트 2: 열화상 기반 데이터 품질 진단 및 불량 판별 실습

본 실습은 KAMP에서 제공하는 머신비전 AI 데이터셋을 활용하여, 제품 열화상 데이터를 분석하고 불량 여부를 자동 진단하는 과정을 학습합니다.

## 🎯 실습 목표
- 제품 열화상 데이터로부터 주요 온도 벡터 추출
- 전처리를 통해 관심 영역만 추출
- 기준값을 바탕으로 양품/불량품 라벨링
- SVM 모델 학습을 통한 불량 예측

## 📁 데이터 구조
- `left_data.csv` / `right_data.csv`: (1차 or 2차 가공) 열화상 온도 벡터 데이터
- `left_label.json` / `right_label.json`: 두께 또는 판정 라벨
- `left_label.csv` / `right_label.csv`: json 기반의 csv 변환 버전

## 🧪 실습 단계
1. 데이터 로딩 및 시각화
2. 전처리 (Masking, Skeleton, ROI 추출)
3. 양품/불량 기준 라벨 생성 (두께 기준: 0.8mm~1.5mm → 양품)
4. SVM 모델 학습 및 성능 평가
5. 오분류 제품 시각화 및 리뷰

## 🔧 분석 환경
- Python 3.9+
- 주요 라이브러리: `numpy`, `pandas`, `matplotlib`, `opencv-python`, `scikit-learn`, `skimage`, `json`
