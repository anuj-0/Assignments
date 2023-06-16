from airflow import DAG
from airflow.models import DagRun
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import psycopg2

# Default arguments for tasks
default_args = {
    "retries": 3,
    "retry_delay": timedelta(seconds=10)
}

# Function to create a table with two columns for storing date and time
def create_table_task():
    conn = psycopg2.connect(
        host='postgres',
        port='5432',
        dbname='airflow',
        user='airflow',
        password='airflow'
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dag_exec_time (
            Execution_date DATE,
            Execution_time TIME
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Function to add the latest execution date and time to the table
def add_entry_to_table_task():
    conn = psycopg2.connect(
        host='postgres',
        port='5432',
        dbname='airflow',
        user='airflow',
        password='airflow'
    )
    cursor = conn.cursor()
    dag_runs = DagRun.find(dag_id="my_db_dag")
    dag_runs.sort(key=lambda x: x.execution_date, reverse=True)
    curr_exec_info = dag_runs[0].execution_date
    curr_exec_date, curr_exec_time = str(curr_exec_info).split(" ")
    cursor.execute(f"""
        INSERT INTO dag_exec_time VALUES (
            '{curr_exec_date}', '{curr_exec_time}'
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

# DAG properties
dag = DAG(
    dag_id="my_db_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="*/2 * * * *",
    default_args=default_args,
    catchup=False
)

# Task 1: Creating the table
create_table = PythonOperator(
    task_id="create_table_task",
    python_callable=create_table_task,
    dag=dag
)

# Task 2: Adding entries to the table
add_entry_in_table = PythonOperator(
    task_id="add_entry_to_table_task",
    python_callable=add_entry_to_table_task,
    dag=dag
)

# Defining dependencies between tasks
create_table >> add_entry_in_table
