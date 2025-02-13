# cli.py
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Atomic Nexus AI CLI")
    parser.add_argument('--run', action='store_true', help="Run the main application")
    args = parser.parse_args()
    if args.run:
        print("Running Atomic Nexus AI CLI")

if __name__ == "__main__":
    main()