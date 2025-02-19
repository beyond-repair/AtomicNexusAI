# AtomicNexusAI/ide/debugger/execution_tracer.py

import time
import logging

logger = logging.getLogger(__name__)

class ExecutionTracer:
    def trace(self, func, *args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        logger.info(f"Function {func.__name__} executed in {exec_time:.4f} seconds")
        print(f"Execution time: {exec_time:.4f} seconds")
        return result