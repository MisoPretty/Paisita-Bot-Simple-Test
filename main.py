import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["backtest", "live", "dashboard"], required=True)
    args = parser.parse_args()
    
    print(f"✅ Bot starting in {args.mode} mode!")
    print("✅ This works!")
    if args.mode == "backtest":
        print("📊 Backtest stub completed")
    elif args.mode == "live":
        print("🔴 Live trading stub started")
    elif args.mode == "dashboard":
        print("🌐 Dashboard stub started")

if __name__ == "__main__":
    main()
