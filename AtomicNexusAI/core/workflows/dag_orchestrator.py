# dag_orchestrator.py
import networkx as nx
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

logger = logging.getLogger(__name__)

class DAGOrchestrator:
    def __init__(self) -> None:
        self.execution_graph = nx.DiGraph()

    def add_task(self, task: object, preconditions: Optional[list] = None) -> None:
        if preconditions:
            self.execution_graph.add_edges_from([(p, task) for p in preconditions])
        self.execution_graph.add_node(task)

    def optimize_path(self) -> list:
        return nx.dag_longest_path(self.execution_graph)

    def execute(self) -> None:
        with ThreadPoolExecutor() as executor:
            for layer in nx.topological_generations(self.execution_graph):
                futures = {executor.submit(t.execute): t for t in layer}
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        self.handle_failure(futures[future])
                        logger.error("Task failed: %s", e)

    def handle_failure(self, task: object) -> None:
        logger.error("Task %s failed. Retrying...", task)