from datetime import datetime

from airflow import DAG
from airflow.operators import bash

from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

default_args = {
    'owner'             : 'rtn',
    'start_date'        : datetime(2024 , 2 , 1),
    "depends_on_past"   : True
}

with DAG(
    dag_id="deverlop_model",
    schedule="*/10 * * * *",
    catchup=False,
    tags=["rtn-AI"],
    default_args=default_args
) as dag :

    date = str(datetime.now()).split(" ")[0]
    
    StartJobs = bash.BashOperator(
        task_id='StartJob',
        bash_command=f"""
            echo StartJob &&
            mkdir -p /airflow_base/Data/AI/{date} &&
            mkdir -p /airflow_base/Data/AI/{date}/data &&
            mkdir -p /airflow_base/Data/AI/{date}/model
        """
    )

    DataSets = DockerOperator(
        task_id='data_sets',
        image="python:3.8",
        container_name="data_sets",
        command=f"bash /task/script.sh ",
        api_version="auto",
        docker_url="unix:///var/run/docker.sock",
        # docker_url="tcp://container-server:2375",
        xcom_all=False,
        network_mode="bridge",
        auto_remove=True,
        mount_tmp_dir=False,
        mounts=[
            Mount(source=f"/airflow_base/Data/AI/input_data_sets/" , target="/input_service/" , type="bind"),
            Mount(source=f"/airflow_base/Data/AI/{date}/data" , target="/output_service/" , type="bind"),
            Mount(source=f"/airflow_base/dags/Docker/AI/1-DataSets/" , target="/task/" , type="bind"),
        ], 
    )

    PrepareDataSets = DockerOperator(
        task_id='prepare_data_set',
        image="python:3.8",
        container_name="prepare_data_set",
        command="bash /task/script.sh ",
        api_version="auto",
        docker_url="unix:///var/run/docker.sock",
        # docker_url="tcp://container-server:2375",
        xcom_all=False,
        network_mode="bridge",
        auto_remove=True,
        mount_tmp_dir=False,
        mounts=[
            Mount(source=f"/airflow_base/Data/AI/{date}/data" , target="/input_service/" , type="bind"),
            Mount(source=f"/airflow_base/Data/AI/{date}/data" , target="/output_service/" , type="bind"),
            Mount(source=f"/airflow_base/dags/Docker/AI/2-PrepareDataSet/" , target="/task/" , type="bind"),
        ], 
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