import sys, os

sys.path.insert(
    0,
    os.path.join(
       '..',
       os.path.dirname(os.path.abspath(__file__))
    )
)

import random
from handler.worker import celery_app


@celery_app.task(bind=True, name='task_test')
def task_test(self):
    n = 10000
    total = 0
    for i in range(0, n):
        total += random.randint(1, 1000)
    return total / n
