from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'salman',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        dag_id="my_first_dag_v",
        description="this is my first dag",
        start_date=datetime(2023, 1, 1),
        schedule_interval='@daily',
        default_args=default_args
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello worlds, this is the first task of mine.'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hey, I am second task and will be executed after first task!'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hey, I am third task and will be ececuted after first task!'
    )
    # task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # task dependency method 3
    task1 >> [task2, task3]
