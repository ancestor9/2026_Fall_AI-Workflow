## AI 활용 학습 커리큘럼

애플리케이션 배포 기초부터 AI 워크플로우 자동화, 최신 AI 에이전트 개념과 실습까지 단계적으로 다루는 커리큘럼입니다.

### 1. App Deployment (애플리케이션 배포 기초)

- **Git & GitHub 기본**: 계정 생성, Git 설치 및 GitHub Desktop을 활용한 코드 버전 관리와 원격 저장소 업로드 방법 습득
- **CI/CD 파이프라인 구축**: 코드 변경 시 자동으로 테스트 및 배포되는 CI/CD 개념을 이해하고, GitHub Actions를 통해 Python+Gradio 앱을 Hugging Face Spaces에 자동 배포하는 실습 수행
- **Docker 컨테이너화**: 애플리케이션을 가상화된 컨테이너로 패키징하여 배포하는 법을 익히고, GitHub Codespaces 클라우드 환경에서 Docker 환경 구축 실습

### 2. What is AI Workflow? (워크플로우와 자동화의 이해)

- **자동화의 본질**: 데이터 기반의 예측 가능한 실행 세트를 통해 사람이 반복하는 작업을 최소화하는 과정 이해
- **워크플로우 구성 요소**: 실행을 시작하는 Trigger, 데이터를 선별하는 Filter, 실제 작업을 수행하는 Action의 구조 학습
- **FastAPI & 스케줄링**: Python 기반의 FastAPI와 BackgroundScheduler를 사용하여 10초마다 작업을 수행하는 로컬 제어 서버 'Hermes Cron' 개발 실습

### 3. Workflow Orchestration Framework (데이터 파이프라인 관리)

- **오케스트레이션 도구**: 복잡한 데이터 파이프라인을 효율적으로 관리하기 위한 Prefect, Dagster, Airflow 프레임워크 소개
- **Prefect 실습**: `@task`와 `@flow` 데코레이터를 사용하여 작업을 정의하고, `.map()` 기능을 통해 여러 데이터를 병렬로 자동 처리하는 워크플로우 구축
- **Airflow 실습**: 데이터를 자산(Asset) 단위로 관리하는 Asset-based Orchestration 개념을 익히고, 데이터 저장 경로 정의 및 웹 대시보드 모니터링 수행

### 4. AI Agent Coding (AI 코딩 에이전트와 실무)

- **Cline (AI 개발 어시스턴트)**: VS Code 플러그인인 Cline을 설치하여 LLM이 직접 코드를 작성, 수정, 실행하고 디버깅까지 수행하는 에이전트 환경 구축
- **Vibe Coding (바이브 코딩)**: 요구사항을 텍스트로 명확히 정의(Spec Coding)하고 AI와 대화하며 웹 페이지 구조와 스타일을 잡아가는 새로운 개발 방식 실습
- **MCP (Model Context Protocol)**: AI 에이전트가 브라우저 제어 등 외부 도구와 통신할 때 사용하는 특화된 프로토콜인 MCP의 개념과 직접 서버를 구축하는 방법 학습

### 5. AI Workflow_n8n (노코드 기반 AI 자동화)

- **n8n 환경 구축**: WSL2, Ubuntu, Docker Desktop을 활용하여 로컬 환경에 n8n 서버를 설치하고 무료로 사용하는 방법
- **노드(Node) 기반 설계**: 실행 시점인 Entry point, 데이터 가공인 Function, 결과 생성인 Exit point 노드를 조합하여 복잡한 자동화 시나리오 구성
- **RAG 파이프라인**: 구글 드라이브의 문서 변경을 감지하여 텍스트를 추출하고, Supabase 벡터 DB에 저장한 뒤 AI 에이전트가 이를 검색하여 답변하는 RAG 시스템 구현

### 6. AI Agents (인공지능 에이전트의 미래)

- **머신러닝의 진화**: 데이터에서 규칙을 찾는 머신러닝부터 확률적으로 다음 단어를 예측하는 **LLM(대규모 언어 모델)** 의 원리 이해
- **AI 에이전트의 정의** : 단순히 텍스트만 생성하는 챗봇을 넘어, 스스로 추론(Reasoning)하고 외부 도구를 사용(Tool-calling)하며 루프를 통해 목표를 완수하는 능력을 갖춘 모델
- **활용 사례** : 빠른 리서치를 돕는 NotebookLM, 대규모 지식 검색을 위한 벡터 DB/RAG, 장기 지식 축적을 위한 LLM 나무위키 등의 활용 전략
