from AtomicNexusAI.security.audit.anomaly_detector import AnomalyDetector


def test_detection():
    detector = AnomalyDetector()
    logs = ["All good", "Error: something failed", "Warning: check system"]
    anomalies = detector.detect(logs)
    assert "Error: something failed" in anomalies
    assert "All good" not in anomalies
