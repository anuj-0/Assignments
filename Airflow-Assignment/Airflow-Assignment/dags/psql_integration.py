import airflow
from datetime import timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

args = {'owner': 'airflow'}

default_args = {
    'owner': 'airflow',
    # 'start_date': airflow.utils.dates.days_ago(2),
    # 'end_date': datetime(),
    # 'depends_on_past': False,
    # 'email': ['airflow@example.com'],
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag_psql = DAG(
    dag_id="postgresoperator_demo",
    default_args=args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@once',
    dagrun_timeout=timedelta(minutes=60),
    description='use case of psql operator in airflow',
    start_date=airflow.utils.dates.days_ago(1)
)

create_employee_table = PostgresOperator(
    task_id="create_employee_table",
    postgres_conn_id="postgres_local",
    sql="sql/employee_schema.sql",
    dag=dag_psql
)
populate_employee_table = PostgresOperator(
    task_id="populate_employee_table",
    postgres_conn_id="postgres_local",
    sql="sql/insert_employee.sql",
    dag=dag_psql
)

get_all_employee = PostgresOperator(
    task_id="get_all_employees",
    postgres_conn_id="postgres_local",
    sql="SELECT * FROM employee;",
    dag=dag_psql
)

create_employee_table >> populate_employee_table >> get_all_employee

if __name__ == "__main__":
    dag_psql.cli()
