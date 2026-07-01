#!/usr/bin/env python3
"""Minimal client for the EnsoTrade live crypto order-flow API (https://www.ensotrade.tech/v1)."""
import json
import urllib.request

BASE = "https://www.ensotrade.tech/v1"


def get(path: str):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "ensotrade-api-example"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())


def explain(coin: str):
    """Why a coin is up or down right now, with a quotable summary."""
    return get(f"/explain/{coin}")


def funding(coin: str):
    """Funding rate, crowding, open interest, perp basis."""
    return get(f"/funding/{coin}")


def orderflow(coin: str):
    """Order-flow regime, taker imbalance, open-interest change."""
    return get(f"/orderflow/{coin}")


if __name__ == "__main__":
    coin = "btc"
    print("WHY:       ", explain(coin).get("summary") or explain(coin).get("answer"))
    print("FUNDING:   ", funding(coin).get("summary"))
    print("ORDER FLOW:", orderflow(coin).get("summary"))
