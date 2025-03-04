# performance_tracer.py
import time

class PerformanceTracer:
    def trace(self, func: callable, *args, **kwargs) -> any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} executed in {end - start:.4f} seconds")
        return result