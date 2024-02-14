import time
from datetime import datetime

with open('/output_service/datasets.txt' , 'r') as file :
    time.sleep(5)
    print("READ DATA : " , file.read() , " timestamp : " , datetime.now())
    with open('/output_service/prepare.txt' , 'w') as file :
        file.write(f"prepare : {datetime.now()}")