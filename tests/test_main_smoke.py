import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_main_demo_smoke():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "main.py")],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stderr
    assert "Claim-0 demo" in proc.stdout
    assert "anomalies:" in proc.stdout
