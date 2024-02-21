# Airflow Auto Install
- Execute
  ```bash
  docker-compose up -d
  ```
- Open on 
  - Airflow Web UI http://localhost:8080

  - Cadvisor http://localhost:8081

- Folder Stucture of Data Input - Output
  ```ruby
  |_airflow_base_
                 |_Data_
  ```

### Werning
- When system notifies an about permission dockerd-entrypoint.sh
  ```bash
  chmod 777 ./data-docker/dockerd-entrypoint.sh
  ```