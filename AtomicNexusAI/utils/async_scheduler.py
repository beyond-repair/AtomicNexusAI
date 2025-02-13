# async_scheduler.py
import asyncio
import logging
from typing import Callable, Any, List, Tuple

logger = logging.getLogger(__name__)

class AsyncTaskScheduler:
    """
    A simple asynchronous task scheduler using asyncio.
    """
    def __init__(self) -> None:
        self.tasks: List[Tuple[Callable[[], Any], int]] = []

    def add_task(self, task: Callable[[], Any], delay: int) -> None:
        """
        Schedule a task to be run after a given delay in seconds.
        
        :param task: A callable representing the task.
        :param delay: Delay in seconds before task execution.
        """
        self.tasks.append((task, delay))
        logger.info("Added async task %s with delay %d seconds.", task.__name__, delay)

    async def _run_task(self, task: Callable[[], Any], delay: int) -> None:
        await asyncio.sleep(delay)
        try:
            logger.info("Running async task %s...", task.__name__)
            result = task()
            logger.info("Task %s completed with result: %s", task.__name__, result)
        except Exception as e:
            logger.error("Async task %s failed: %s", task.__name__, e)

    async def run(self) -> None:
        """
        Run all scheduled tasks concurrently.
        """
        logger.info("Starting async execution of %d tasks.", len(self.tasks))
        await asyncio.gather(*(self._run_task(task, delay) for task, delay in self.tasks))
        logger.info("All async tasks have completed.")

> Usage Example:
In your code (or CLI), you can import and use this scheduler as follows:

import asyncio
from utils.async_scheduler import AsyncTaskScheduler

def sample_task():
    print("Hello from async task!")
    return "Done"

scheduler = AsyncTaskScheduler()
scheduler.add_task(sample_task, 3)
asyncio.run(scheduler.run())