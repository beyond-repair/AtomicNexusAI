class AnomalyDetector:
    def detect(self, logs: list) -> list:
        return [log for log in logs if "error" in log.lower()]
