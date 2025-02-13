# kubernetes_mgr.py

class KubernetesManager:
    def deploy(self, task: object) -> None:
        print(f"Deploying task {task} to Kubernetes cluster.")