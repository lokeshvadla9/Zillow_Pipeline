from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime

#Importing the etl function
from zillow_etl import run_zillow_etl

#Airflow DAG properties
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 8),
    'email': ['john.doe@domain.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

#creating DAG
dag = DAG(
    'zillow_dag',
    default_args=default_args,
    description='first DAG with ETL process!',
    #scheduling the job to run once in every 31 days
    schedule_interval=timedelta(days=31),
)

run_etl = PythonOperator(
    task_id='complete_zillow_etl',
    python_callable=run_zillow_etl,
    dag=dag, 
)

run_etl