# Airflow Auto Install
- Execute
  ```
  docker-compose up -d
  ```
- Open on 
  - Airflow Web UI http://localhost:8080

  - Cadvisor http://localhost:8081

- Folder Stucture of Docker Server
  ```
  |_pipeline
  ```

### Werning
- When system notifies an about permission dockerd-entrypoint.sh
  ```
  chmod 777 ./data-docker/dockerd-entrypoint.sh
  ```