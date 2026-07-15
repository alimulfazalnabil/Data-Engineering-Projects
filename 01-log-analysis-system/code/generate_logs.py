import datetime
import os
import random
import time

LOG_DIR = './logs'
os.makedirs(LOG_DIR, exist_ok=True)

while True:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    level = random.choice(['INFO', 'WARN', 'ERROR'])
    msg = f'User action {random.randint(1, 100)}'
    log_line = f'{timestamp} [{level}] {msg}\n'
    with open(os.path.join(LOG_DIR, 'app.log'), 'a', encoding='utf-8') as f:
        f.write(log_line)
    time.sleep(1)
