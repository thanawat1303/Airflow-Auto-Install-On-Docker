# Airflow Auto Install
- Execute
  ```bash
  docker-compose up -d
  ```
- Open on 
  - Airflow Web UI http://localhost:8080

  - Cadvisor http://localhost:8081

- Folder Stucture
  - PythonOparetor
    ```ruby
    |_airflow_base_
                  |_dags_
                         |_Python
    ```

  - DockerOparetor
    ```ruby
    |_airflow_base_
                  |_dags_
                         |_Docker
    ```

  - Data : Input , Output
    ```ruby
    |_airflow_base_
                   |_Data_
    ```

  - Python Module
    ```ruby
    |_airflow_base_
                   |_dags_
                          |_Python_
    ```
  
### Example Tasks
- PythonOperator
  ```python
  from airflow.operators.python import PythonOperator
  Example = PythonOperator(
      task_id='task-python',
      python_callable=function,
      op_args=[args]
  )
  ```

- DockerOperator
  - Run on Host
    ```python
    from airflow.providers.docker.operators.docker import DockerOperator
    Example = DockerOperator(
        task_id='task-docker',
        image="docker:tag",
        api_version="auto",
        docker_url="unix:///var/run/docker.sock",
        network_mode="bridge",
        mounts=[
            Mount(source=f"/airflow_base/Data/" , target="/input_service/" , type="bind"), #input
            Mount(source=f"/airflow_base/Data/" , target="/output_service/" , type="bind"), #output
            Mount(source=f"/airflow_base/dags/Docker/" , target="/task/" , type="bind"), #module
        ], 
    )
    ```
  
  - Run on Container server
    ```python
    from airflow.providers.docker.operators.docker import DockerOperator
    Example = DockerOperator(
        task_id='task-docker',
        image="docker:tag",
        api_version="auto",
        docker_url="tcp://container-server:2375",
        network_mode="bridge",
        mounts=[
            Mount(source=f"/airflow_base/Data/" , target="/input_service/" , type="bind"), #input
            Mount(source=f"/airflow_base/Data/" , target="/output_service/" , type="bind"), #output
            Mount(source=f"/airflow_base/dags/Docker/" , target="/task/" , type="bind"), #module
        ], 
    )
    ```

### Werning
- When system notifies an about permission dockerd-entrypoint.sh
  ```bash
  chmod 777 ./data-docker/dockerd-entrypoint.sh
  ```

### Referrent
- https://airflow.apache.org/