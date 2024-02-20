from datetime import datetime
import time

from airflow import DAG
from airflow.operators import bash , python

default_args = {
    'owner'             : 'rtn',
    'start_date'        : datetime(2024 , 2 , 1),
    'depend_on_part'    : True
}

def data_set(date_input) :
    with open('/airflow_base/pipe/data/input_data_sets/data.txt' , 'r') as file :
        time.sleep(5)
        print("READ DATA : " , file.read() , " timestamp : " , datetime.now())
        with open(f'/airflow_base/pipe/data/{date_input}/data/datasets_python.txt' , 'w') as file :
            file.write(f"DataSets : {datetime.now()}")

def prepare_data(date_input) :
    with open(f'/airflow_base/pipe/data/{date_input}/data/datasets_python.txt' , 'r') as file :
        time.sleep(5)
        print("READ DATA : " , file.read() , " timestamp : " , datetime.now())
        with open(f'/airflow_base/pipe/data/{date_input}/data/prepare_python.txt' , 'w') as file :
            file.write(f"prepare : {datetime.now()}")

with DAG(
    dag_id="deverlop_model_python",
    schedule="*/30 * * * *",
    catchup=False,
    tags=["rtn-AI"],
    default_args=default_args
) as dag :

    date = str(datetime.now()).split(" ")[0]
    
    StartJobs = bash.BashOperator(
        task_id='StartJob',
        bash_command=f"""
            echo StartJob && 
            if [ ! -e '/airflow_base/pipe/data/{date}' ]; then
                mkdir /airflow_base/pipe/data/{date} 
            fi && 
            if [ ! -e '/airflow_base/pipe/data/{date}/data' ]; then
                mkdir /airflow_base/pipe/data/{date}/data
            fi && 
            if [ ! -e '/airflow_base/pipe/data/{date}/model' ]; then
                mkdir /airflow_base/pipe/data/{date}/model
            fi
        """
    )

    DataSets = python.PythonOperator(
        task_id='data_sets',
        python_callable=data_set,
        op_args=[date]
    )

    PrepareDataSets = python.PythonOperator(
        task_id='prepare_data_set',
        python_callable=prepare_data,
        op_args=[date]
    )

    AfterPrepare1 = bash.BashOperator(
        task_id='Prepare1',
        bash_command="echo Prepare1"
    )

    AfterPrepare2 = bash.BashOperator(
        task_id='Prepare2',
        bash_command="echo Prepare2"
    )

    StartJobs >> DataSets >> PrepareDataSets

    PrepareDataSets >> [AfterPrepare1 , AfterPrepare2]