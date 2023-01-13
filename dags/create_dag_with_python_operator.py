from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f'Hello World, my name is {first_name} {last_name} and I am {age} years old!')


def get_name(ti):
    ti.xcom_push(key='first_name', value='Harry')
    ti.xcom_push(key='last_name', value='Potter')


def get_age(ti):
    ti.xcom_push(key='age', value=33)


default_args = {
    'owner': 'salman',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        dag_id='dag_with_python_operator_v8',
        description='my first dag for using python operator in airflow dags',
        start_date=datetime(2023, 1, 1),
        schedule_interval='@daily',
        default_args=default_args

) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        # op_kwargs={'age': 34}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
