execution_tracer.py
import time

class ExecutionTracer:
    def trace(self, func, *args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} executed in {end - start:.4f} seconds")
        return result