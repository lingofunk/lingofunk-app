# Copy from distributedpython.com/2018/07/03/simple-celery-setup/

"""
before running this script:
- install celery
    pip install celery
- start celery:
    celery worker --app=worker.celery_app --concurrency=1 --pool=solo --loglevel=INFO
- restart celery after changes in source files!

"""


import os
from celery import Celery

import sys

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..'
    )
)

def find_project_root_dir():
    def get_last_part(path): 
        return os.path.basename(os.path.normpath(path))

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    cur_path = THIS_FOLDER

    for i in range(5):
        if get_last_part(cur_path) in ["clustering_system", "build"]:
            break
        cur_path = os.path.dirname(cur_path)
    else:
        raise ValueError("cannot find clustering_system")
    return cur_path


folder_root = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..'
)
folder_handler = os.path.join(folder_root, 'handler')
folder_broker = os.path.join(folder_handler, 'broker')

broker_url = 'filesystem://'

for f in ['out', 'processed']:
    if not os.path.exists(os.path.join(folder_broker, f)):
        os.makedirs(os.path.join(folder_broker, f))


celery_app = Celery(__name__)

celery_app.conf.update({
    'broker_url': broker_url,
    'broker_transport_options': {
        'data_folder_in': os.path.join(folder_broker, 'out'),
        'data_folder_out': os.path.join(folder_broker, 'out'),
        'data_folder_processed': os.path.join(folder_broker, 'processed')
    },
    'imports': ('tasks',),
    'result_persistent': False,
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})

