from AtomicNexusAI.core.models.adaptive_selector import AdaptiveSelector
from AtomicNexusAI.core.models.model_manager import ModelManager


def test_adaptive_selector_default():
    selector = AdaptiveSelector()
    assert selector.select_model(object()) == "default_model"


def test_model_manager_register_get():
    mgr = ModelManager()
    mgr.register_model("m1", {"kind": "stub"})
    assert mgr.get_model("m1") == {"kind": "stub"}
    assert mgr.get_model("missing") is None
