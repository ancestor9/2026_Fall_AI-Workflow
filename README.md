# AI 활용 학습 커리큘럼

애플리케이션 배포 기초부터 AI 워크플로우 자동화, 최신 AI 에이전트 개념과 실습까지 단계적으로 다루는 커리큘럼입니다.

## 1. App Deployment (애플리케이션 배포 기초)

- **Git & GitHub 기본**: 계정 생성, Git 설치 및 GitHub Desktop을 활용한 코드 버전 관리와 원격 저장소 업로드 방법 습득
- **CI/CD 파이프라인 구축**: 코드 변경 시 자동으로 테스트 및 배포되는 CI/CD 개념을 이해하고, GitHub Actions를 통해 Python+Gradio 앱을 Hugging Face Spaces에 자동 배포하는 실습 수행
- **Docker 컨테이너화**: 애플리케이션을 가상화된 컨테이너로 패키징하여 배포하는 법을 익히고, GitHub Codespaces 클라우드 환경에서 Docker 환경 구축 실습

## 2. What is AI Workflow? (워크플로우와 자동화의 이해)

- **자동화의 본질**: 데이터 기반의 예측 가능한 실행 세트를 통해 사람이 반복하는 작업을 최소화하는 과정 이해
- **워크플로우 구성 요소**: 실행을 시작하는 Trigger, 데이터를 선별하는 Filter, 실제 작업을 수행하는 Action의 구조 학습
- **FastAPI & 스케줄링**: Python 기반의 FastAPI와 BackgroundScheduler를 사용하여 10초마다 작업을 수행하는 로컬 제어 서버 'Hermes Cron' 개발 실습

## 3. Workflow Orchestration Framework (데이터 파이프라인 관리)

- **오케스트레이션 도구**: 복잡한 데이터 파이프라인을 효율적으로 관리하기 위한 Prefect와 Dagster 프레임워크 소개
- **Prefect 실습**: `@task`와 `@flow` 데코레이터를 사용하여 작업을 정의하고, `.map()` 기능을 통해 여러 데이터를 병렬로 자동 처리하는 워크플로우 구축
- **Dagster 실습**: 데이터를 자산(Asset) 단위로 관리하는 Asset-based Orchestration 개념을 익히고, 데이터 저장 경로 정의 및 웹 대시보드 모니터링 수행

## 4. AI Agent Coding (AI 코딩 에이전트와 실무)

-
