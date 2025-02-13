# anomaly_detector.py

class AnomalyDetector:
    def detect(self, logs: list[str]) -> list[str]:
        anomalies = [log for log in logs if "error" in log.lower()]
        return anomalies