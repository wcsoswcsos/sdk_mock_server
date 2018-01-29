import os

WORK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

HTTPS_KEY = os.path.join(WORK_DIR,'res','certificate','ca.key')
HTTPS_CRT = os.path.join(WORK_DIR,'res','certificate','ca.crt')
