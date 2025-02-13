task_scheduler.py
import time
from threading import Thread

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, delay):
        self.tasks.append((task, delay))

    def start(self):
        for task, delay in self.tasks:
            Thread(target=self._run_task, args=(task, delay)).start()

    def _run_task(self, task, delay):
        time.sleep(delay)
        try:
            task.execute()
        except Exception as e:
            print(f"Task {task} failed: {e}")