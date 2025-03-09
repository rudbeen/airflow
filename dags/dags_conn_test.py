from airflow import DAG 
import pendulum
import datetime 
# from airflow.operators.empty import EmptyOperator
from airflow.operators.dummy import DummyOperator

with DAG(
    dag_id = "dags_conn_test",
    schedule_interval=None,
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    
    t1 = DummyOperator(
        task_id = "t1"
    )

    t2 = DummyOperator(
        task_id = "t2"
    )

    t3 = DummyOperator(
        task_id = "t3"
    )
    t4 = DummyOperator(
        task_id = "t4"
    )
    t5 = DummyOperator(
        task_id = "t5"
    )
    t6 = DummyOperator(
        task_id = "t6"
    )
    t7 = DummyOperator(
        task_id = "t7"
    )
    t8 = DummyOperator(
        task_id = "t8"
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8