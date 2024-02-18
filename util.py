import time
import random

def random_sleep(duration):
    percentage = 0.2 # 20%
    range_value = duration * percentage
    min_duration = duration - range_value
    max_duration = duration + range_value
    random_duration = round(random.uniform(min_duration, max_duration), 2)
    time.sleep(random_duration)