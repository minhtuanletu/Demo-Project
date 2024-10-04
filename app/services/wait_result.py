import redis
import time
from config import *

connection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

def wait_result(task, id_task):
    while True:
        try:
            key = f'result:{task}:{id_task}'
            value = connection.get(key)
            if value is not None:
                connection.delete(key)
                return value.decode('utf-8')
            time.sleep(1)
        except:
            print('Not have key!')
            continue