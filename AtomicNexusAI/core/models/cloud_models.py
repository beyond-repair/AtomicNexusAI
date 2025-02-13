# cloud_models.py

class CloudModel:
    def __init__(self, model_id: str) -> None:
        self.model_id = model_id

    def predict(self, data: any) -> str:
        return f"CloudModel {self.model_id} prediction for {data}"