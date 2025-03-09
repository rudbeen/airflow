from datetime import timedelta
import pendulum 

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='dags_bash_operator',   ### 파이썬 파일명과는 무관하지만 DAG 이름을 일치시키는 것이 좋음 
    default_args=args,
    schedule_interval='0 0 * * *',    ### 분 / 시 / 일 / 월 / 요일 - 0시 0분 매일 
    # start_date=days_ago(2),    ### 2일 전부터 
    start_date = pendulum.datetime(2023, 3, 1, tz='Asia/Seoul'),
    catchup=False, ### 가급적 False로 두는게 좋음 
    # params ={"example_key": "example_value"},    ### 테스크들에 공통적으로 넘겨줄 변수
) as dag:
    
    bash_t1 = BashOperator(
        task_id='bash_t1',    ### 화면에 나타나는 값 / bash 명과 task_id는 일치하게끔 설정하는 것이 좋음 
        bash_command='echo whoami',
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',    ### 화면에 나타나는 값 / bash 명과 task_id는 일치하게끔 설정하는 것이 좋음 
        bash_command='echo $HOSTNAME',
    )
    
    bash_t1 >> bash_t2