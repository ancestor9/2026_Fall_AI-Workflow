import time
from prefect import task, flow

@task(name="데이터 다운로드")
def fetch_data(source_name: str):
    print(f"[{source_name}]에서 데이터 다운로드 시작...")
    time.sleep(2)  # 다운로드 시뮬레이션
    return f"{source_name} raw data"

@task(name="데이터 전처리")
def preprocess_data(raw_data: str):
    print(f"'{raw_data}' 정제 및 노이즈 제거 중...")
    time.sleep(1.5)
    return f"Cleaned {raw_data}"

@task(name="최종 앙상블 모델 검증")
def train_and_evaluate(data_list: list):
    print("모든 전처리 데이터 결합 중...")
    for data in data_list:
        print(f"-> 통합 데이터셋에 {data} 포함 완료")
    time.sleep(3)
    print("최종 모델 평과 결과: Accuracy 94.5%")
    return "Success"

# log_prints=True로 설정해야 UI의 Logs 탭에서 각 task의 print문을 볼 수 있습니다.
@flow(name="ML-Pipeline-Visualization-Demo", log_prints=True)
def ml_pipeline():
    sources = ["AWS_S3", "Google_Cloud", "Local_DB"]
    
    # 1. 병렬 다운로드 진행
    # 파이썬 리스트 컴프리헨션을 사용해 task를 호출하면 UI에서 세 개가 나란히 실행됩니다.
    raw_datasets = [fetch_data(source) for source in sources]
    
    # 2. 다운로드된 각 데이터를 순서대로 전처리
    # UI 그래프에서 다운로드 task와 전처리 task가 1:1로 연결됩니다.
    cleaned_datasets = [preprocess_data(dataset) for dataset in raw_datasets]
    
    # 3. 모든 전처리 결과를 모아서 최종 모델 평가
    # 3개의 전처리 task 줄기가 하나로 모이는 시각적 효과를 볼 수 있습니다.
    final_result = train_and_evaluate(cleaned_datasets)
    
    print(f"전체 파이프라인 실행 상태: {final_result}")

if __name__ == "__main__":
    # Prefect 로컬 서버가 켜져 있고(prefect server start)
    # API 주소가 설정되어 있다면(prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api")
    # 실행 시 자동으로 UI에 연동됩니다.
    ml_pipeline()