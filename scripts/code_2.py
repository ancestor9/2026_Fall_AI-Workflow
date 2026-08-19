from pathlib import Path
import numpy as np
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# 💡 Flow 클래스 대신 flow 데코레이터를 가져옵니다.
from prefect import task, flow 

@task
def download_dataset():
    print('download_dataset begin')
    dataset_filename = 'dataset.csv'
    random_state = np.random.RandomState(seed=17)
    a, b = random_state.uniform(-10, 10, 2)
    x_data = random_state.uniform(-10, 10, size=100)
    y_data = a * x_data + b + random_state.uniform(-10, 10, size=100)
    dataset = np.column_stack((x_data, y_data))
    np.savetxt(dataset_filename, dataset, delimiter=',')
    print('download_dataset end')
    return dataset_filename

@task
def preprocess_dataset(dataset_filename):
    print('preprocess_dataset begin')
    train_dataset_filename = f'train_{dataset_filename}'
    test_dataset_filename = f'test_{dataset_filename}'
    dataset = np.loadtxt(dataset_filename, delimiter=',')
    x_train, x_test, y_train, y_test = train_test_split(
        dataset[:, 0], dataset[:, 1], random_state=23)
    train_dataset = np.column_stack((x_train, y_train))
    test_dataset = np.column_stack((x_test, y_test))
    np.savetxt(train_dataset_filename, train_dataset, delimiter=',')
    np.savetxt(test_dataset_filename, test_dataset, delimiter=',')
    print('preprocess_dataset end')
    # 💡 최신 버전에서는 튜플을 그대로 반환하는 것이 안전합니다.
    return train_dataset_filename, test_dataset_filename

@task
def train_model(train_dataset_filename):
    print('train_model begin')
    model_filename = str(
        Path(f'model_{train_dataset_filename}').with_suffix('.joblib'))
    dataset = np.loadtxt(train_dataset_filename, delimiter=',')
    model = LinearRegression().fit(dataset[:, 0:1], dataset[:, 1])
    dump(model, model_filename)
    print('train_model end')
    return model_filename

@task
def evaluate_model(model_filename, test_dataset_filename):
    print('evaluate_model begin')
    eval_model_filename = str(Path(f'eval_{model_filename}').with_suffix('.txt'))
    model = load(model_filename)
    dataset = np.loadtxt(test_dataset_filename, delimiter=',')
    score = model.score(dataset[:, 0:1], dataset[:, 1])
    np.savetxt(eval_model_filename, [score])
    print('evaluate_model end')
    return eval_model_filename

# 💡 최신 버전의 Flow 정의 방식: 함수 위에 @flow를 붙입니다.
# log_prints=True를 주면 함수 내부의 print()문이 Prefect UI 로그에도 예쁘게 찍힙니다.
@flow(name="code_2_flow", log_prints=True)
def main_flow():
    dataset_filename = download_dataset()
    
    # Task가 복수 개의 값을 반환할 때 최신 Prefect에서는 아래와 같이 처리하는 것이 좋습니다.
    train_test_filenames = preprocess_dataset(dataset_filename)
    train_file = train_test_filenames[0]
    test_file = train_test_filenames[1]
    
    model_filename = train_model(train_file)
    eval_model_filename = evaluate_model(model_filename, test_file)
    
    print('dataset_filename', dataset_filename)
    print('model_filename', model_filename)
    print('eval_model_filename', eval_model_filename)

if __name__ == "__main__":
    print('flow run begin')
    # 💡 구버전의 flow.run() 대신, 일반 파이썬 함수처럼 호출하면 대시보드에 기록됩니다.
    main_flow()
    print('flow run end')