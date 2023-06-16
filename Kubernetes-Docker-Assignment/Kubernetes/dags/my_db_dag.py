from airflow import DAG
from airflow.models import DagRun
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import psycopg2


# PROPERTIES OF TASKS
default_args = {"retries":3,
                "retry_delay":timedelta(seconds=10)}

# FUNCTION TO CREATE A TABLE WITH TWO COLUMNS FOR STORING DATE AND TIME
def Create_postgres_table():
     conn = psycopg2.connect(
        host='postgres',
        port='5432',
        dbname='airflow',
        user='airflow',
        password='airflow'
    )
     cursor = conn.cursor()
     cursor.execute("""
                    CREATE TABLE IF NOT EXISTS dag_exec_time(
                        Execution_date DATE,
                        Execution_time TIME
                    );
             """)
     conn.commit()
     cursor.close()
     conn.close()
  
# FUNCTION TO ADD LATEST EXECUTION DATE AND TIME
def Add_entry_to_table():
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
                    INSERT INTO dag_exec_time VALUES(
                        '{curr_exec_date}', '{curr_exec_time}'
                    );
             """)
     conn.commit()
     cursor.close()
     conn.close()
     
# PROPERTIES OF DAG
dag = DAG(dag_id="my_db_dag",
         start_date=datetime(2023,1,1),
         schedule_interval="*/2 * * * *",
         default_args=default_args,
         catchup=False)
    
# TASK-1 CREATING TABLE
create_table = PythonOperator(
    task_id="Create_postgres_table",
    python_callable=Create_postgres_table,
    dag=dag
)

# TASK-2 ADDING ENTRIES TO TABLE
insert_entry_in_table = PythonOperator(
    task_id="Add_entry_to_table",
    python_callable=Add_entry_to_table,
    dag=dag
)

# DEFINING DEPENDENCIES BETWEEN TASKS
create_table >> insert_entry_in_table
