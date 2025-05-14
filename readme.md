# 과정: 입문자를 위한 Chatgpt 및 API 활용 서비스 제작 실무
- 교육시간: 2일, 14시간 / 09:30 ~ 17:30

# 커리큘럼
***
## [Phase 01] OpenAI API 소개 및 기초 서비스 제작
- OpenAI API 개요 (계정 생성)
- 실습환경 준비, chatGPT (무료, 유료면 better)
- 멀티모달 API 기초 서비스 실습
  - OpenAI 연계서비스(이미지, TTS, 자동 요약 등)
- 다중 API 연계 서비스 개발
  - Dalle-3, TTS, ChatGPT 연계
  - Whisper, ChatGPT 연계
  
## [Phase 02] 다중 API 연계서비스 개발 및 GPT 개인화
- 텍스트 → 구조화 → 멀티모달 연결
  : 텍스트 → 오디오(TTS), 텍스트 → 이미지 생성(DALL·E), 음성 → 텍스트(Whisper) 등이 하나의 파이프라인화
- GPT 개인화 구현(개인용 챗봇)
- GPTs

***

# (Day1) Phase 01 상세내용

## OpenAI API 개요
- openai의 공식 Playground에서 실제 실습할 환경을 미리 경험해보기
  (https://platform.openai.com/playground/prompts?models=gpt-3.5-turbo)

- openai의 공식 docs guide 문서의 QuickStart를 해보는 실습 (https://platform.openai.com/docs/guides)

- Key Concepts: 모델 종류 (GPT-4, DALL·E, Whisper 등) / 엔드포인트 구조
- 실시간 데모: Playground 활용으로 간단한 프롬프트 실습?


## 실습환경 준비
- 코드 환경: VS Code, Python venv
- 필수 패키지: openai.OpenAI, dotenv.load_dotenv, os
- .env 파일 : OPENAI_API_KEY 지정 (https://platform.openai.com/settings/organization/api-keys)

## Quickstart 기본 실습 1, 2, 3
- Developer quickstart

## 멀티모달 API
- 이미지 생성 (DALL·E 3) 및 음성 생성 (TTS) 구조 설명
- API 응답 포맷 구조 강조

## OpenAI 연계서비스 예시
- 이미지 + 텍스트 통합: 이미지 생성 후 설명 생성
- TTS, STT

## 다중 API 연계
- 실습코드 함수화, pipeline 생성

# (Day2) Phase 02 상세내용

## Streamlit Quickstart 기본 실습 1, 2, 3
- https://docs.streamlit.io/
- 텍스팅, DataFrame 처리, 차트그리기, Input Widget 만들기, Layout 생성

## GPT ChatBot 구현
- Streamlit 사용 : EchoBot --> OpenAI 직접 연동
- https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps
- 개인화된 GPT 만들기

## GPT 확장 사례 소개
- RAG
- Langchain
- MCP


