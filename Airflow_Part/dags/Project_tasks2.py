from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta



#from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 1),
    #'retries': 1,
}


# Define the DAG
with DAG(
    dag_id='Simple_Corona_project',
    default_args=default_args,
    description='A simple python project to filter data and make some operations using PySpark',
    schedule_interval=timedelta(minutes=40),  # Run once a day
    catchup=False,  # to prevent the dag from trying to run agian and catch days it didnt run
) as dag:

    # Define the Bash task
    task1 = BashOperator(
        task_id='Produce_data',
        bash_command="""
        cd /opt/airflow/dags/CoronaProj/
        python3 API_CALL.py
        """,
        
    )


    task2 = BashOperator(
        task_id='Spark_Processing',
        bash_command='''
        cd /opt/airflow/dags/CoronaProj/
        spark-submit --jars "/opt/airflow/dags/CoronaProj/postgresql-42.7.5.jar" Spark_script_process.py
        ''',
    )


    
    task1 >> task2 

    

    # You can add more tasks here and set dependencies

# You can add dependencies between tasks like this:
# task1 >> task2
