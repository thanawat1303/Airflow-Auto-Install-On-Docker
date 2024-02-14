import time
from datetime import datetime

with open('/input_service/data.txt' , 'r') as file :
    time.sleep(5)
    print("READ DATA : " , file.read() , " timestamp : " , datetime.now())
    with open('/output_service/datasets.txt' , 'w') as file :
        file.write(f"DataSets : {datetime.now()}")