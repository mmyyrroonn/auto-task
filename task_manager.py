import random
from datetime import datetime
from tinydb import TinyDB, Query
from logger import logger
from util import parse_date

class DailyTaskManager:
    def __init__(self) -> None:
        self.history = TinyDB('daily-history.json')
        pass

    def get_today_datestring(self):
        # Get today's date
        today = datetime.now()
        
        # Format the date as a string in the format 'YYYY-MM-DD'
        date_string = today.strftime('%Y-%m-%d')
        
        return date_string

    def build_task_list(self, user_list, task_func_with_option_list, disable_history=False):
        datestring = self.get_today_datestring()
        tasks = []
        for user in user_list:
            for (task_func, option, todo_users) in task_func_with_option_list:
                if disable_history or not self.is_task_completed(datestring, user["acc_id"], task_func.__name__):
                    if user["acc_id"] in todo_users:
                        tasks.append({"date": datestring, "func": task_func, "user": user, "option": option})
        random.shuffle(tasks)
        logger.info("Total tasks count is {}".format(len(tasks)))
        return tasks
    
    def handle_result(self, result, task):
        """
        Store or update the task completion result in the database.
        If an identical task entry exists, it updates that entry.
        Otherwise, it inserts a new entry into the database.
        """
        TaskQuery = Query()
        # Search for an existing task with the same date, acc_id, and func_name
        search_result = self.history.search(
            (TaskQuery.date == task["date"]) & 
            (TaskQuery.acc_id == task["user"]["acc_id"]) & 
            (TaskQuery.func_name == task["func"].__name__)
        )
        
        # Data to be inserted or updated
        task_data = {
            'date': task["date"],
            'acc_id': task["user"]["acc_id"],
            'func_name': task["func"].__name__,
            'completed': result
        }
        
        if search_result:
            # Update the existing task with the new result and increment the 'tries' count
            existing_doc_id = search_result[0].doc_id
            current_tries = search_result[0].get('tries', 1)  # Default to 1 if 'tries' does not exist
            self.history.update(task_data | {'tries': current_tries + 1}, doc_ids=[existing_doc_id])
        else:
            # Insert a new task entry with 'tries' initialized to 1
            self.history.insert(task_data | {'tries': 1})
    
    def is_task_completed(self, datestring, acc_id, task_name):
        TaskQuery = Query()
        # Search for an existing task with the same date, acc_id, and func_name
        search_result = self.history.search(
            (TaskQuery.date == datestring) & 
            (TaskQuery.acc_id == acc_id) & 
            (TaskQuery.func_name == task_name)
        )
        
        if search_result:
            completed = search_result[0].get('completed', True)  # Default to 1 if 'tries' does not exist
            return completed
        return False
    
class OnceTaskManager:
    def __init__(self, db_name = "once-history.json", wait_day = 2) -> None:
        self.history = TinyDB(db_name)
        self.wait_day = wait_day
        pass

    def get_today_datestring(self):
        # Get today's date
        today = datetime.now()
        
        # Format the date as a string in the format 'YYYY-MM-DD'
        date_string = today.strftime('%Y-%m-%d')
        
        return date_string

    def build_task_list(self, user_list, task_func_with_option_list, disable_history=False):
        datestring = self.get_today_datestring()
        tasks = []
        for user in user_list:
            if self.is_user_skip(datestring, user["acc_id"]):
                continue
            random.shuffle(task_func_with_option_list)
            for (task_func, option, todo_users) in task_func_with_option_list:
                if disable_history or not self.is_task_skip(datestring, user["acc_id"], task_func.__name__):
                    if user["acc_id"] in todo_users:
                        tasks.append({"date": datestring, "func": task_func, "user": user, "option": option})
                        break # Just one task for one user one time
        random.shuffle(tasks)
        logger.info("Total tasks count is {}".format(len(tasks)))
        return tasks
    
    def handle_result(self, result, task):
        """
        Store or update the task completion result in the database.
        If an identical task entry exists, it updates that entry.
        Otherwise, it inserts a new entry into the database.
        """
        TaskQuery = Query()
        # Search for an existing task with the same date, acc_id, and func_name
        search_result = self.history.search(
            (TaskQuery.date == task["date"]) & 
            (TaskQuery.acc_id == task["user"]["acc_id"]) & 
            (TaskQuery.func_name == task["func"].__name__)
        )
        
        # Data to be inserted or updated
        task_data = {
            'date': task["date"],
            'acc_id': task["user"]["acc_id"],
            'func_name': task["func"].__name__,
            'completed': result
        }
        
        if search_result:
            # Update the existing task with the new result and increment the 'tries' count
            existing_doc_id = search_result[0].doc_id
            current_tries = search_result[0].get('tries', 1)  # Default to 1 if 'tries' does not exist
            self.history.update(task_data | {'tries': current_tries + 1}, doc_ids=[existing_doc_id])
        else:
            # Insert a new task entry with 'tries' initialized to 1
            self.history.insert(task_data | {'tries': 1})
    
    def is_task_skip(self, datestring, acc_id, task_name):
        TaskQuery = Query()
        # Search for an existing task with the same date, acc_id, and func_name
        search_result = self.history.search(
            (TaskQuery.acc_id == acc_id) & 
            (TaskQuery.func_name == task_name)
        )
        
        if search_result:
            completed = search_result[0].get('completed', True)  # Default to 1 if 'tries' does not exist
            return completed
        return False
    def is_user_skip(self, todaystring, acc_id):
        TaskQuery = Query()
        # Search for an existing task with the same date, acc_id, and func_name
        search_result = self.history.search(
            (TaskQuery.acc_id == acc_id)
        )

        # Step 2: Check if we have at least one task and get its date
        if search_result:
            # Step 1: Sort the search_result by date (assuming each item in search_result is an instance of Task)
            search_result.sort(key=lambda task: task.get('date'), reverse=True) # Sorts in descending order, most recent first
            status = search_result[0].get('completed', False)
            if not status:
                return False

            most_recent_date = parse_date(search_result[0].get('date'))

            # Step 3: Compare with today's date
            today = parse_date(todaystring)
            delta_days = (today - most_recent_date).days

            if delta_days < self.wait_day:
                return True
            else:
                return False
        else:
            # No tasks found, handle accordingly
            return False  # or False, depending on your requirement