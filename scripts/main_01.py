import datetime
from fastapi import FastAPI
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler

# 1. FastAPI 애플리케이션 생성
app = FastAPI(
    title="Hermes Agent Cron Server",
    description="VS Code 로컬 환경에서 구동하는 에이전트 크론 서버"
)

# 2. 백그라운드 스케줄러 및 로그 저장소 세팅w   
scheduler = BackgroundScheduler()
job_logs = []

# 3. 크론(Cron) 타이머가 울릴 때마다 실행할 함수 정의
def my_cron_job():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_msg = f"⏰ [Cron] {now} - 백그라운드 자동화 작업 완료!"
    print(log_msg)  # VS Code 터미널 콘솔에 즉시 출력됨
    job_logs.append(log_msg)


# 4. FastAPI 서버가 시작될 때 스케줄러도 함께 실행하도록 설정
@app.on_event("startup")
def start_scheduler():
    # 로컬에서 눈으로 바로 확인하기 위해 10초 주기(*/10)로 크론 등록
    scheduler.add_job(my_cron_job, 'cron', second='*/10')
    scheduler.start()
    print("🚀 백그라운드 크론 스케줄러가 성공적으로 시작되었습니다! (10초 주기)")

# 5. FastAPI 서버가 닫힐 때 스케줄러도 안전하게 종료
@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()
    print("🛑 스케줄러가 안전하게 종료되었습니다.")

# 6. API 엔드포인트(라우터) 정의
@app.get("/")
def read_root():
    return {
        "status": "running", 
        "message": "VS Code 로컬 서버가 정상 작동 중입니다."
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

# 7. VS Code에서 이 파일(`python main.py`)을 직접 실행할 수 있도록 진입점 설정
if __name__ == "__main__":
    # uvicorn을 통해 8000번 포트로 서버를 엽니다.
    # reload=True를 주면 코드를 수정하고 저장할 때마다 서버가 자동으로 재시작됩니다.
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)