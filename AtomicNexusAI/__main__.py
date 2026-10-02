"""Allow `python -m AtomicNexusAI` to run the Claim-0 demo."""
from pathlib import Path
import runpy
import sys

# Delegate to repo-root main.py when present; otherwise inline minimal demo.
root_main = Path(__file__).resolve().parents[1] / "main.py"
if root_main.is_file():
    sys.argv[0] = str(root_main)
    runpy.run_path(str(root_main), run_name="__main__")
else:
    from AtomicNexusAI.config.logging_config import setup_logging
    from AtomicNexusAI.config.config_manager import load_config
    import main as root  # type: ignore

    setup_logging()
    cfg_path = Path(__file__).resolve().parent / "config" / "default_settings.yaml"
    raise SystemExit(root.run_demo(load_config(str(cfg_path))))
