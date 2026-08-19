import subprocess
from prefect import flow, task
from prefect.futures import PrefectFuture
import sys

@task(log_prints=True)
def run_script(script_name: str):
    """Runs a Python script and captures output."""
    print(f"Starting {script_name}...")
    # 기존: subprocess.run(["python", script_name])
    # 변경: 현재 가상환경의 파이썬 인터프리터 경로(sys.executable)를 사용
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{script_name} completed successfully.")
        print(result.stdout)
    else:
        print(f"{script_name} failed with error:")
        print(result.stderr)
        raise RuntimeError(f"{script_name} failed")
    return result.stdout


@flow(log_prints=True)
def orchestrator_flow():
    # Step 1: Submit Code1, Code2, Code3 in parallel
    future1: PrefectFuture = run_script.submit("Code1.py")
    future2: PrefectFuture = run_script.submit("Code2.py")
    future3: PrefectFuture = run_script.submit("Code3.py")

    # Step 2: Wait for all three to complete
    future1.wait()
    future2.wait()
    future3.wait()

    # Step 3: Run Code4 sequentially after the parallel ones finish
    run_script("Code4.py")

    # Step 4: Run Code5 after Code4
    run_script("Code5.py")


if __name__ == "__main__":
    orchestrator_flow()