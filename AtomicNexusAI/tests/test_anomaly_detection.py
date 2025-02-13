test_anomaly_detection.py
import unittest
from security.audit.anomaly_detector import AnomalyDetector

class TestAnomalyDetection(unittest.TestCase):
    def test_detection(self):
        detector = AnomalyDetector()
        logs = ["All good", "Error: something failed", "Warning: check system"]
        anomalies = detector.detect(logs)
        self.assertIn("Error: something failed", anomalies)

if __name__ == '__main__':
    unittest.main()