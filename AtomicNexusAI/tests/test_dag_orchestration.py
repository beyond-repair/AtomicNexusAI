# test_dag_orchestration.py
import unittest
from core.workflows.dag_orchestrator import DAGOrchestrator

class DummyTask:
    def execute(self) -> None:
        print("Executing DummyTask")

class TestDAGOrchestrator(unittest.TestCase):
    def test_dag_execution(self) -> None:
        dag = DAGOrchestrator()
        task1 = DummyTask()
        task2 = DummyTask()
        dag.add_task(task1)
        dag.add_task(task2, preconditions=[task1])
        dag.execute()

if __name__ == '__main__':
    unittest.main()