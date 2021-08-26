import datetime
import time

halloween2016 = datetime.datetime(2021, 8, 20, 15, 5, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
