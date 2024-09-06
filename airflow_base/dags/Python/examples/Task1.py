from datetime import datetime
import time

def Task1(**key) :
    with open(key["input"] , 'r') as file :
        time.sleep(5)
        print("READ DATA : " , file.read() , " timestamp : " , datetime.now())
        with open(key["output"] , 'w') as file :
            file.write(f"DataSets : {datetime.now()}")