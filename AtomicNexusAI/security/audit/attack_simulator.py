# attack_simulator.py
import argparse

def simulate_attack(strict_mode: bool = False) -> None:
    print("Simulating attack...")
    if strict_mode:
        print("Strict mode enabled: simulating severe attack conditions.")
    print("Attack simulation complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-mode', action='store_true', help="Enable strict mode simulation")
    args = parser.parse_args()
    simulate_attack(strict_mode=args.strict_mode)