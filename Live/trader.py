
import time
import pandas as pd

from data.kalshi_scraper import KalshiScraper
from data.polymarket_scraper import PolymarketScraper
from ml.model import ProbabilityModel

def run_live_trading(config:dict):

    ks=KalshiScraper(
        api_key=config["kalshi"]["api_key"],
        private_key=config["kalshi"]["private_key"],
        base_url=config["kalshi"]["base_url"],
    )

    ps=PolymarketScraper(base_url=config["polymarket"]["base_url"])

    model=ProbabilityModel()

    print("Starting live trading loop (stub). Ctrl+C to stop.")

    while True:

        snap_k=ks.fetch_markets_snapshot()
        snap_p=ps.fetch_markets_snapshot()

        snapshot=pd.concat([snap_k,snap_p],ignore_index=True)

        if snapshot.empty:
            print("No markets.")
        else:

            probs=model.predict_proba(snapshot)
            edges=model.compute_edges(snapshot)

            snapshot["prob_yes"]=probs
            snapshot["edge_yes"]=edges

            min_edge=float(config["strategy"]["min_edge"])
            max_edge=float(config["strategy"]["max_edge"])

            candidates=snapshot[
                (snapshot["edge_yes"].abs()>=min_edge) &
                (snapshot["edge_yes"].abs()<=max_edge)
            ]

            print("Candidate trades:")
            print(candidates[[
                "platform","market_id","question","yes_price","prob_yes","edge_yes"
            ]])

        time.sleep(30)
