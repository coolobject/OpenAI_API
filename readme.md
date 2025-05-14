# 과정: 입문자를 위한 Chatgpt 및 API 활용 서비스 제작 실무 (<https://www.kpc.or.kr/PTWED003_dtil_view.do?ecno=45501>)

## 교육시간: 2일, 14시간 / 09:30 ~ 17:30

## 교육장소: 한국생산성본부 8층 803호

## 교육비: 정상가 620,000 원 KPC 유료법인회원 560,000 원

## 교육문의: ICT교육센터 02-724-1218 / <hkypark@kpc.or.kr> / 결제·계산서문의 : 02-724-1212

# 커리큘럼

***
## [Phase 01] OpenAI API 소개 및 기초 서비스 제작

- OpenAI API 개요 (계정 생성)
- 실습환경 준비, chatGPT (무료, 유료면 better)
- 멀티모달 API
- 기초 서비스 실습 준비
- OpenAI 연계서비스(이미지, TTS, 자동 요약 등)

## [Phase 02] 다중 API 연계서비스 개발 및 GPT 개인화

- 다중 API 연계 서비스 개발
- Dalle-3, TTS, ChatGPT 연계
- Whisper, ChatGPT 연계
- 텍스트 → 구조화 → 멀티모달 연결
  : 텍스트 → 오디오(TTS), 텍스트 → 이미지 생성(DALL·E), 음성 → 텍스트(Whisper) 등이 하나의 파이프라인화
- GPT 개인화 구현(개인용 챗봇)
- GPTs

***

# Phase 01 상세내용

## OpenAI API 개요
- openai의 공식 Playground에서 실제 실습할 환경을 미리 경험해보기
  (https://platform.openai.com/playground/prompts?models=gpt-3.5-turbo)

- openai의 공식 docs guide 문서의 QuickStart를 해보는 실습 (https://platform.openai.com/docs/guides)

- Key Concepts: 모델 종류 (GPT-4, DALL·E, Whisper 등) / 엔드포인트 구조
- 실시간 데모: Playground 활용으로 간단한 프롬프트 실습?


## 실습환경 준비

- 코드 환경: VS Code + Python venv
- 필수 패키지: openai.OpenAI, dotenv.load_dotenv, os
- .env 파일 : OPENAI_API_KEY 지정 (https://platform.openai.com/settings/organization/api-keys)

## Quickstart 기본 실습 1, 2, 3
- Developer quickstart
  - Generate text from a model (https://platform.openai.com/docs/quickstart?api-mode=responses)
  - Analyze the content of an image (https://platform.openai.com/docs/quickstart#analyze-image-inputs)
  - Extend the model with tools (https://platform.openai.com/docs/quickstart#extend-the-model-with-tools) : 오늘 뉴스, 날씨 등 웹서치 가능함 (외부 도구 사용), gpt-4.1 이상 모델 가능 (gpt-4.1-nano는 지원 안 됨)


## 멀티모달 API

- 이미지 생성 (DALL·E 3) 및 음성 생성 (TTS) 구조 설명
- API 응답 포맷 구조 강조

## 기초 서비스 실습

- 예: "질문 요약기", "이미지 설명 서비스" 제작
- 실습 목표는 API 호출 구조 이해 + 간단한 결과 시각화

## OpenAI 연계서비스 예시

- 이미지 + 텍스트 통합: 이미지 생성 후 설명 생성
- TTS: 텍스트 → 음성 후 저장 및 재생 (ex. pyttsx3, edge-tts 활용)

# Phase 02 상세내용

## 다중 API 연계

- ex. 사용자가 녹음 → Whisper로 텍스트 변환 → GPT로 요약
- 서비스 시나리오 기반 (ex. 회의록 요약기)

## DALL·E, TTS, ChatGPT 통합

- 프롬프트 설계에 따라 결과가 어떻게 달라지는지 강조
- 실제 서비스와 유사한 UI 시나리오 구성 (ex. Gradio or Streamlit)

## GPT 개인화 구현

- system 메시지를 이용한 역할 고정
- Function Calling or tools 기능 간단 소개

## GPTs & GPT Store 소개

- 개인화된 GPT 만들기 (gpts.openai.com 사용법)
- 사용 예시: FAQ 응답 챗봇, 업무 자동화 비서 등
