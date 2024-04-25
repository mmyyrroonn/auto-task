import time
import random
from datetime import datetime

def random_sleep(duration):
    percentage = 0.2 # 20%
    range_value = duration * percentage
    min_duration = duration - range_value
    max_duration = duration + range_value
    random_duration = round(random.uniform(min_duration, max_duration), 2)
    time.sleep(random_duration)

def parse_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').date()

# def update_db():
#     users = load_users_list()
#     history = TinyDB('once-history.json')
#     for user in users:
#         print(user)
#         TaskQuery = Query()
#         # Search for an existing task with the same date, acc_id, and func_name
#         search_result = history.search(
#             (TaskQuery.acc_id == user["user_id"])
#         )
#         print(search_result)
#         for item in search_result:
#             # Update the existing task with the new result and increment the 'tries' count
#             existing_doc_id = item.doc_id
#             history.update({'acc_id': user["acc_id"]}, doc_ids=[existing_doc_id])