import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler

# 1. 백그라운드 스케줄러 및 로그 저장소 세팅
scheduler = BackgroundScheduler()
job_logs = []

# 크론(Cron) 타이머가 울릴 때마다 실행할 함수 정의
def my_cron_job():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_msg = f"⏰ [Cron] {now} - 백그라운드 자동화 작업 완료!"
    print(log_msg)  # VS Code 터미널 콘솔에 즉시 출력됨
    job_logs.append(log_msg)

# 2. Lifespan 이벤트 핸들러 정의 (시작과 종료를 한 번에 관리)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---- [STARTUP] 서버가 켜질 때 실행되는 구간 ----
    # 10초 주기(*/10)로 크론 작업을 등록하고 스케줄러를 시작합니다.
    scheduler.add_job(my_cron_job, 'cron', second='*/10')
    scheduler.start()
    print("🚀 백그라운드 크론 스케줄러가 성공적으로 시작되었습니다! (10초 주기)")
    
    yield  # 💻 이 yield를 기점으로 서버가 정상 구동되며 대기합니다.
    
    # ---- [SHUTDOWN] 서버가 꺼질 때 실행되는 구간 ----
    # VS Code에서 Ctrl + C를 누르면 이 아랫줄이 실행됩니다.
    scheduler.shutdown()
    print("🛑 스케줄러가 안전하게 종료되었습니다.")


# 3. FastAPI 애플리케이션 생성 (lifespan 핸들러 등록)
app = FastAPI(
    title="Hermes Agent Cron Server",
    description="Lifespan 방식을 적용한 에이전트 크론 서버",
    lifespan=lifespan
)


# 4. API 엔드포인트(라우터) 정의
@app.get("/")
def read_root():
    return {
        "status": "running", 
        "message": "VS Code 로컬 서버가 정상 작동 중입니다. (Lifespan 적용 완료)"
    }

@app.get("/logs")
def get_logs():
    """크론 작업이 실행된 기록을 확인하는 API"""
    return {"total_runs": len(job_logs), "history": job_logs}

@app.post("/trigger")
def trigger_now():
    """예약된 시간과 별개로 사용자가 API를 통해 즉시 작업을 트리거"""
    my_cron_job()
    return {"message": "⚡ 에이전트 작업을 즉시 강제 실행했습니다."}


# 5. VS Code에서 직접 실행 진입점
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)