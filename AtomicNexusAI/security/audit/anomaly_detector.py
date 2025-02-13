anomaly_detector.py

class AnomalyDetector:
    def detect(self, logs):
        # Dummy detection logic
        anomalies = [log for log in logs if "error" in log.lower()]
        return anomalies