from datetime import datetime

from airflow import DAG
from airflow.operators import bash , python

from AI_module import data_sets , prepare

default_args = {
    'owner'             : 'rtn',
    'start_date'        : datetime(2024 , 2 , 1),
    "depends_on_past"   : True
}

with DAG(
    dag_id="deverlop_model_python",
    schedule="*/1 * * * *",
    start_date=datetime(2024 , 2 , 20),
    catchup=False,
    tags=["rtn-AI"],
    default_args=default_args
) as dag :

    date = str(datetime.now()).split(" ")[0]
    
    A = bash.BashOperator(
        task_id='A',
        bash_command=f"""
            echo StartJob && 
            mkdir -p /airflow_base/Data/AI/{date} &&
            mkdir -p /airflow_base/Data/AI/{date}/data &&
            mkdir -p /airflow_base/Data/AI/{date}/model
        """
    )

    B = python.PythonOperator(
        task_id='B',
        python_callable=data_sets.data_set,
        op_kwargs={
            'input' : "/airflow_base/Data/AI/input_data_sets/data.txt",
            'output' : f"/airflow_base/Data/AI/{date}/data/datasets_python.txt"
        }
    )

    C = python.PythonOperator(
        task_id='C',
        python_callable=prepare.prepare_data,
        op_kwargs={
            'input' : f"/airflow_base/Data/AI/{date}/data/datasets_python.txt",
            'output' : f"/airflow_base/Data/AI/{date}/data/datasets_python.txt"
        }
    )

    D = bash.BashOperator(
        task_id='D',
        bash_command="echo Prepare1"
    )

    E = bash.BashOperator(
        task_id='E',
        bash_command="echo Prepare2"
    )

    A >> B >> C
    C >> [D , E]