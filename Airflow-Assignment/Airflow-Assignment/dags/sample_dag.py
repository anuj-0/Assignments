from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.email_operator import EmailOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'example_email_notification',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

# Define a dummy task that always succeeds
dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)

# Define an email operator to send a notification when the dummy task succeeds
email_notification = EmailOperator(
    task_id='email_notification',
    dag=dag,
    to='anuj.mohan@sigmoidanalytics.com',
    subject='Airflow DAG Notification',
    html_content='The dummy task has succeeded!'
)

# Set the dependencies between the tasks
dummy_task >> email_notification
