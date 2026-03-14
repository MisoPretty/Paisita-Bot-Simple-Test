
import pandas as pd
from data.kalshi_scraper import KalshiScraper
from data.polymarket_scraper import PolymarketScraper
from ml.model import ProbabilityModel

def run_backtest(config:dict):

    ks=KalshiScraper(
        api_key=config["kalshi"]["api_key"],
        private_key=config["kalshi"]["private_key"],
        base_url=config["kalshi"]["base_url"],
    )

    ps=PolymarketScraper(base_url=config["polymarket"]["base_url"])

    hist_k=ks.fetch_historical(
        config["backtest"]["start_date"],
        config["backtest"]["end_date"]
    )

    hist_p=ps.fetch_historical(
        config["backtest"]["start_date"],
        config["backtest"]["end_date"]
    )

    historical=pd.concat([hist_k,hist_p],ignore_index=True)

    model=ProbabilityModel()
    model.fit(historical)

    print("Backtest completed (stub). Rows:",len(historical))
