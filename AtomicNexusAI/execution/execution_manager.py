# execution_manager.py
from .local.resource_allocator import ResourceAllocator
from .cloud.cloud_connector import CloudConnector
from .cloud.cost_aware_offloading import CloudOffloadOptimizer
import logging

logger = logging.getLogger(__name__)

class ExecutionManager:
    def __init__(self) -> None:
        self.local_allocator = ResourceAllocator()
        self.cloud_connector = CloudConnector()
        self.offload_optimizer = CloudOffloadOptimizer()

    def execute_task(self, task: object) -> None:
        try:
            if self.offload_optimizer.should_offload(task):
                logger.info("Offloading task to cloud.")
                self.cloud_connector.connect()
                # Here you could call an AWSRunner or KubernetesManager method
            else:
                logger.info("Executing task locally.")
                self.local_allocator.allocate(task)
                task.execute()
        except Exception as e:
            logger.error("Error executing task: %s", e)