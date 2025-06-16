# 🧰 실습 전 준비사항

이 문서는 Wiki.js 또는 AWS WorkDocs를 활용하여 제조 데이터 거버넌스 문서화 실습을 진행하기 위해 필요한 사전 준비 항목을 안내합니다.

---

## ✅ 공통 준비 사항

- GitHub 레포지토리 `manufacturing-data-lab` 클론 또는 다운로드
- Markdown 편집 가능한 텍스트 에디터 설치 (예: VS Code, Obsidian, Typora 등)
- 문서 작성 가이드를 이해하기 위한 사전 읽기:
  - `00_common/templates/` 내 기준 문서 템플릿 확인
  - `00_common/tools_guide/airflow_glue_compare.md` 확인

---

## 🖥 Wiki.js 사용 시

### 1. 시스템 요구 사항
- Docker 설치된 로컬 환경 또는 클라우드 서버
- 최소 사양: 2 vCPU, 4GB RAM

### 2. 설치 참고자료
- `00_common/tools_guide/wikijs_setup.md` 문서 참고

### 3. 실행 전 체크리스트
- Wiki.js 서버 실행 완료 (Docker 또는 Node 설치 방식)
- 관리자 계정 생성 및 로그인 확인
- 문서 카테고리 생성 권한 확보
- Markdown 업로드 또는 WYSIWYG 작성 기능 확인

---

## ☁️ AWS WorkDocs 사용 시

### 1. 계정 및 조직 설정
- AWS WorkDocs 조직 생성 (관리자 권한 필요)
- 사용자 계정 활성화 및 로그인 확인

### 2. 폴더 구조 준비
- 기준 문서 업로드용 전용 폴더 생성 (예: `/제조데이터-기준정의`)
- 팀원 간 공유 및 권한 설정 완료

### 3. 파일 호환성
- `.md`, `.docx`, `.pdf` 등 주요 포맷 확인
- 댓글, 승인 기능이 사용 가능한지 점검

---

## 🧪 실습 전 점검 항목

| 항목 | 점검 여부 |
|------|-----------|
| 기준 문서 템플릿 확인 완료 | ✅ / ❌ |
| 문서화 도구 중 하나 설치 완료 (Wiki.js or WorkDocs) | ✅ / ❌ |
| 실습 계정 및 권한 설정 완료 | ✅ / ❌ |
| 공정/품질 관련 간단한 사례 이해 | ✅ / ❌ |

---

## 📂 실습에 활용될 폴더 위치

- 실습 기준 문서 위치:
  - `01_governance_framework/wiki_output/`
  - `01_governance_framework/workdocs_output/`
- 문서 작성 후 제출 위치:
  - PR 또는 업로드 지시사항에 따라 제출

---

## 📝 기타 안내

- 본 실습은 향후 품질 진단 및 자동화 실습과 연계됩니다. 작성한 기준 문서는 후속 실습에서 그대로 활용되므로 최대한 실제 상황을 염두에 두고 작성해 주세요.
