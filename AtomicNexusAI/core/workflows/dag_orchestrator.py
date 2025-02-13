dag_orchestrator.py
import networkx as nx
from concurrent.futures import ThreadPoolExecutor, as_completed

class DAGOrchestrator:
    def __init__(self):
        self.execution_graph = nx.DiGraph()

    def add_task(self, task, preconditions=None):
        if preconditions:
            self.execution_graph.add_edges_from([(p, task) for p in preconditions])
        self.execution_graph.add_node(task)

    def optimize_path(self):
        return nx.dag_longest_path(self.execution_graph)

    def execute(self):
        with ThreadPoolExecutor() as executor:
            for layer in nx.topological_generations(self.execution_graph):
                futures = {executor.submit(t.execute): t for t in layer}
                for future in as_completed(futures):
                    if future.exception():
                        self.handle_failure(futures[future])

    def handle_failure(self, task):
        print(f"[ERROR] Task {task} failed. Retrying...")