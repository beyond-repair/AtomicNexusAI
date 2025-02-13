cost_aware_offloading.py
from execution.cloud.cloud_pricing_api import CloudPricingAPI
from execution.local.hardware_aware import HardwareAware

# Dummy DecisionModel for demonstration purposes
class DecisionModel:
    def __init__(self, version):
        self.version = version

    def predict(self, factors):
        # Simple decision: offload if cost factor is less than 1
        return factors.get('cost_diff', 1) < 1

def log_decision_rationale(factors, decision, version):
    decision_str = 'Offload' if decision else 'Local execution'
    print(f"DecisionModel v{version}: Factors: {factors}, Decision: {decision_str}")

class CloudOffloadOptimizer:
    def __init__(self):
        self.cloud_pricing = CloudPricingAPI()
        self.hardware_monitor = HardwareAware()
        self.decision_model = DecisionModel(version="1.0")

    def should_offload(self, task):
        cost_matrix = self.cloud_pricing.get_real_time_pricing(task)
        local_perf = self.hardware_monitor.get_local_resources().get("cpu", 1)  # Simplified metric

        factors = {
            'task_priority': getattr(task, 'priority', 1),
            'cost_diff': cost_matrix['cloud'] / cost_matrix['local'],
            'latency_diff': local_perf / cost_matrix['cloud_latency']
        }
        decision = self.decision_model.predict(factors)
        log_decision_rationale(factors, decision, self.decision_model.version)
        return decision