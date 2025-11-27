# Streamlit 마케팅 전략 Agent 시스템

## 📋 프로젝트 개요

Seoul Seongdong-gu Shinhan Card 데이터(4,185개 가맹점)를 활용한 **4개 페이지 구성의 마케팅 전략 Agent 시스템**입니다.

## 🏗️ 폴더 구조

```
streamlit_app/
├── main.py                    # 메인 홈페이지
├── pages/                     # Streamlit 멀티페이지
│   ├── 1_📊_매출_분석.py      # Q1 Agent - 매출 분석
│   ├── 2_👥_고객_분석.py      # Q2 Agent - 고객 분석
│   ├── 3_🎯_마케팅_전략.py    # Q3 Agent - 마케팅 전략
│   └── 4_📈_통합_대시보드.py   # 통합 대시보드
├── utils/                     # 유틸리티 함수들
│   └── helpers.py            # 헬퍼 함수 모음
├── agents/                    # Agent 연결 모듈
│   └── agent_connector.py    # 기존 Agents/ 폴더와 연결
├── .streamlit/               # Streamlit 설정
│   └── config.toml          # 테마 및 서버 설정
└── requirements.txt         # 패키지 의존성
```

## 🎯 페이지 구성

### 1. 🏠 메인 홈페이지 (`main.py`)

- 시스템 소개 및 Agent 개요
- 데이터셋 정보 제공
- 사용법 안내

### 2. 📊 매출 분석 - Q1 Agent

- 매출 트렌드 분석
- 성과 지표 모니터링
- 매출 예측 및 인사이트

### 3. 👥 고객 분석 - Q2 Agent

- 고객 세그멘테이션
- 행동 패턴 분석
- 재방문율 및 충성도 분석

### 4. 🎯 마케팅 전략 - Q3 Agent

- 개인화된 마케팅 전략
- 캠페인 최적화
- ROI 극대화 방안

### 5. 📈 통합 대시보드

- 전체 현황 요약
- Agent 결과 통합
- 트렌드 분석
- 주요 인사이트 및 액션 플랜

## 🚀 실행 방법

### 1. 환경 설정

```bash
cd streamlit_app
pip install -r requirements.txt
```

### 2. 앱 실행

```bash
streamlit run main.py
```

### 3. 브라우저에서 접속

```
http://localhost:8501
```

## 🔗 연결된 구조

### 기존 프로젝트와의 연결

- **데이터 소스**: `../data/` 폴더의 3개 데이터셋
- **분류기**: `../improved_classifier.py`의 `classify_for_agents()` 함수
- **에이전트**: `../Agents/` 폴더의 마케팅 에이전트들
- **대시보드**: `../dashboard/dashboard.py` 활용

### Agent 시스템 연동

- **Q1 Agent**: 매출 데이터 분석 및 예측
- **Q2 Agent**: 고객 행동 패턴 및 세그멘테이션
- **Q3 Agent**: 마케팅 전략 수립 및 최적화

## 📊 데이터 활용

### Dataset 1 (big_data_set1_f.csv)

- 가맹점 기본 정보 (4,185개)
- 업종, 지역 등 메타 데이터

### Dataset 2 (big_data_set2_f.csv)

- 매출 거래 데이터
- 거래량, 금액, 시간 정보

### Dataset 3 (big_data_set3_f.csv)

- 고객 데이터
- 방문 패턴, 세그먼트, 행동 정보

## 🎨 UI/UX 특징

- **멀티페이지 구조**: Streamlit의 네이티브 멀티페이지 지원
- **직관적 네비게이션**: 사이드바 기반 페이지 이동
- **반응형 레이아웃**: 와이드 스크린 최적화
- **실시간 분석**: 가맹점 선택 시 즉시 Agent 실행
- **결과 시각화**: 차트, 테이블, 메트릭 카드

## 🤖 Agent 활용법

1. **가맹점 선택**: 4,185개 가맹점 중 분석 대상 선택
2. **Agent 실행**: 각 페이지에서 해당 Agent 실행 버튼 클릭
3. **결과 확인**: 실시간으로 분석 결과 및 인사이트 제공
4. **통합 대시보드**: 모든 결과를 한눈에 확인

## 🔧 확장 가능성

- **추가 Agent**: 새로운 분석 Agent 쉽게 추가
- **외부 API 연동**: 실시간 데이터 소스 연결
- **알림 시스템**: 중요 인사이트 알림 기능
- **보고서 생성**: PDF/Excel 형태의 보고서 자동 생성

## 📞 지원 및 문의

- **개발팀**: 기술적 이슈 및 버그 신고
- **사용법**: 각 페이지의 도움말 섹션 참고
- **Agent 문의**: Q1/Q2/Q3 Agent 관련 문의
