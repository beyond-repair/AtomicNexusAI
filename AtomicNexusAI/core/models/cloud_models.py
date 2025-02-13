cloud_models.py

class CloudModel:
    def __init__(self, model_id):
        self.model_id = model_id

    def predict(self, data):
        return f"CloudModel {self.model_id} prediction for {data}"