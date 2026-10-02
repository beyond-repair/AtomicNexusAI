from AtomicNexusAI.core.workflows.dag_orchestrator import DAGOrchestrator


class DummyTask:
    def __init__(self, name):
        self.name = name
        self.ran = False

    def execute(self):
        self.ran = True
        return self.name


def test_dag_execution_order():
    dag = DAGOrchestrator()
    t1 = DummyTask("one")
    t2 = DummyTask("two")
    dag.add_task(t1)
    dag.add_task(t2, preconditions=[t1])
    dag.execute()
    assert t1.ran and t2.ran
    path = dag.optimize_path()
    assert t1 in path and t2 in path
