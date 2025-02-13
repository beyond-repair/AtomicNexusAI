# cli.py
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Atomic Nexus AI CLI")
    parser.add_argument('--run', action='store_true', help="Run the main application")
    parser.add_argument('--async', dest='async_mode', action='store_true', help="Run tasks asynchronously")
    args = parser.parse_args()
    
    if args.run:
        mode = "asynchronous" if args.async_mode else "synchronous"
        print(f"Running Atomic Nexus AI CLI in {mode} mode.")
        # Here you could integrate additional interactive options,
        # or choose which task scheduler to use based on the mode.
    else:
        print("No action specified. Use --run to start the application.")

if __name__ == "__main__":
    main()