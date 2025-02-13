# task_scheduler.py
import time
import logging
from threading import Thread

logger = logging.getLogger(__name__)

class TaskScheduler:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: object, delay: int) -> None:
        self.tasks.append((task, delay))

    def start(self) -> None:
        for task, delay in self.tasks:
            Thread(target=self._run_task, args=(task, delay), daemon=True).start()

    def _run_task(self, task: object, delay: int) -> None:
        time.sleep(delay)
        try:
            task.execute()
        except Exception as e:
            logger.error("Task %s failed: %s", task, e)# task_scheduler.py
import time
import logging
from threading import Thread

logger = logging.getLogger(__name__)

class TaskScheduler:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: object, delay: int) -> None:
        self.tasks.append((task, delay))

    def start(self) -> None:
        for task, delay in self.tasks:
            Thread(target=self._run_task, args=(task, delay), daemon=True).start()

    def _run_task(self, task: object, delay: int) -> None:
        time.sleep(delay)
        try:
            task.execute()
        except Exception as e:
            logger.error("Task %s failed: %s", task, e)