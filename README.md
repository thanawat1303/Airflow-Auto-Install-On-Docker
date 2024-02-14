### airflow

## ตั้งตั้ง airflow
- ติดตั้งด้วย docker-compose
- โหลดไฟล์ compose จาก official airflow
- ตั้งตั้ง
  python```
        docker compose up airflow-init # ตั้งตั้ง user pass admin
        docker compose up # ติดตั้ง airflow

        # docker-compose -f /airflow_base/compose.yml up airflow-init -d && docker-compose -f /airflow_base/compose.yml up -d
  ```

## การตั้ง scheduler
 1. กำหนดภายใน DAG ตามนี้
  python```
    DAG(
        dag_id="id_dag",
        schedule="*/5 * * * *" || timedelta(seconds=10),
        catchup=False,
        start_date=datetime(2024 , 2 , 1),
        tags=["rtn-AI"],
        default_args=default_args
    )
  ```

 - dag_id           = ไอดีของ dag
 - start_date       = ตั้งเวลาเริ่มต้นทำงาน
 - schedule         = ตั้งเวลาในการทำงานซ้ำ
 - catchup          = กำหนดว่าต้องการให้ทำงานในส่วนที่เวลาผ่านมาแล้วหรือไม่ True คือให้ทำ False คือ ไม่ให้ทำ
 - tags             = tags ของ dag
 - default_args     = ค่าที่ต้องการกำหนดให้ใช้งานทุก dag หมายเหตุ catchup ไม่สามารถใช้ได้

## ใช้งานร่วมกับ docker
- ประโยชน์
  - เหมาะกับงานที่มีการใช้ package ที่เยอะ เพราะถ้าตามคอนเซ็บของ docker แล้ว การใช้ micro service ในการเป็น base ของ jobs ก็จะช่วยให้ไม่กินทรัพยากรของเครื่องจนเกินไป ใช้เสร็จแล้วทิ้งได้เลย ไม่กินพื้นที่ของเครื่อง host งานที่มีกระบวนการทำงานหรือโค้ดเยอะๆ
- การติดตั้ง
  - 
- การใช้งาน
  - ร่วมกับ DockerOperator
    ```
    ```

### ALPINE
docker run -it alpine /bin/sh
apk add --update docker openrc
rc-update add docker boot
service docker start