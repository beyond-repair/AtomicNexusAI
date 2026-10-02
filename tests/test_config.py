from pathlib import Path

from AtomicNexusAI.config.config_manager import load_config

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "AtomicNexusAI" / "config" / "default_settings.yaml"


def test_load_default_config():
    cfg = load_config(str(DEFAULT))
    assert cfg["app"]["name"] == "Atomic Nexus AI"
    assert "version" in cfg["app"]
