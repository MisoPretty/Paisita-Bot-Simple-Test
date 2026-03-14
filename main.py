
import argparse
import yaml
from pathlib import Path

from backtest.engine import run_backtest
from live.trader import run_live_trading
from dashboard.app import run_dashboard

def load_config():
    with Path("config.yaml").open() as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["backtest","live","dashboard"], required=True)
    args = parser.parse_args()

    config = load_config()

    if args.mode == "backtest":
        run_backtest(config)
    elif args.mode == "live":
        run_live_trading(config)
    elif args.mode == "dashboard":
        run_dashboard(config)

if __name__ == "__main__":
    main()
