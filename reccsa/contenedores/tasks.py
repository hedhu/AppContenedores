from celery import shared_task
from time import sleep

@shared_task
def sleepTest():
    for i in range(10):
        time.sleep(1)
        print(i)
    return "Done"