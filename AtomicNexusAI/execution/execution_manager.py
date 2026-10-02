# execution_manager.py
from .local.resource_allocator import ResourceAllocator
from .cloud.cloud_connector import CloudConnector
from .cloud.cost_aware_offloading import CloudOffloadOptimizer
import logging

logger = logging.getLogger(__name__)


class ExecutionManager:
    """Hybrid local/cloud task runner (Claim-0 stub connectors)."""

    def __init__(self) -> None:
        self.local_allocator = ResourceAllocator()
        self.cloud_connector = CloudConnector()
        self.offload_optimizer = CloudOffloadOptimizer()

    def execute_task(self, task: object) -> dict:
        try:
            if self.offload_optimizer.should_offload(task):
                logger.info("Offloading task to cloud.")
                self.cloud_connector.connect()
                result = task.execute() if hasattr(task, "execute") else None
                return {"mode": "cloud", "result": result}
            logger.info("Executing task locally.")
            self.local_allocator.allocate(task)
            result = task.execute() if hasattr(task, "execute") else None
            return {"mode": "local", "result": result}
        except Exception as e:
            logger.error("Error executing task: %s", e)
            return {"mode": "error", "result": str(e)}
