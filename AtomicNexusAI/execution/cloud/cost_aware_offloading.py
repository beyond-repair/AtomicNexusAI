# cost_aware_offloading.py
from .cloud_pricing_api import CloudPricingAPI
from ..local.hardware_aware import HardwareAware
import logging

logger = logging.getLogger(__name__)

EPSILON = 1e-6  # small constant to avoid division by zero

class DecisionModel:
    def __init__(self, version: str) -> None:
        self.version = version

    def predict(self, factors: dict) -> bool:
        # Offload if the cost ratio is less than 1.
        # Add safeguard to avoid division by zero.
        cost_diff = factors.get('cost_diff', 1)
        return cost_diff < 1 - EPSILON

def log_decision_rationale(factors: dict, decision: bool, version: str) -> None:
    decision_str = 'Offload' if decision else 'Local execution'
    logger.info("DecisionModel v%s: Factors: %s, Decision: %s", version, factors, decision_str)

class CloudOffloadOptimizer:
    def __init__(self) -> None:
        self.cloud_pricing = CloudPricingAPI()
        self.hardware_monitor = HardwareAware()
        self.decision_model = DecisionModel(version="1.0")

    def should_offload(self, task: object) -> bool:
        cost_matrix = self.cloud_pricing.get_real_time_pricing(task)
        local_perf = self.hardware_monitor.get_local_resources().get("cpu", 1)

        factors = {
            'task_priority': getattr(task, 'priority', 1),
            'cost_diff': cost_matrix['cloud'] / (cost_matrix['local'] + EPSILON),
            'latency_diff': local_perf / cost_matrix['cloud_latency']
        }
        decision = self.decision_model.predict(factors)
        log_decision_rationale(factors, decision, self.decision_model.version)
        return decision