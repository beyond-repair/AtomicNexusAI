batch_processor.py

class BatchProcessor:
    def process(self, tasks):
        results = []
        for task in tasks:
            results.append(task.execute())
        return results