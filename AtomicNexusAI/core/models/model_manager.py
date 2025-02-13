# model_manager.py

class ModelManager:
    def __init__(self) -> None:
        self.models = {}

    def register_model(self, name: str, model: object) -> None:
        self.models[name] = model

    def get_model(self, name: str) -> object | None:
        return self.models.get(name)