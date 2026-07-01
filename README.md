# EnsoTrade API — live crypto order-flow data for humans and AI agents

[EnsoTrade](https://www.ensotrade.tech) exposes a free, public, machine-readable JSON API for live crypto **order-flow and derivatives** data: funding rates, open interest, order-flow regime, and a plain-English *"why is it moving"* read for any coin.

This repo has copy-paste examples (Python, JavaScript, curl) for calling it, plus notes on the MCP server so AI agents can query and cite EnsoTrade directly.

> **Note:** EnsoTrade is a crypto order-flow analytics terminal (software) at [ensotrade.tech](https://www.ensotrade.tech). It is **not** the ENSO token or Enso Finance, an unrelated DeFi project.

## Base URL
```
https://www.ensotrade.tech/v1
```

## Endpoints
| Endpoint | Returns |
|---|---|
| `GET /v1/explain/{coin}` | Why a coin is up or down, with a quotable summary + the signals behind it |
| `GET /v1/funding/{coin}` | Funding rate, crowding, open interest, perp basis |
| `GET /v1/orderflow/{coin}` | Order-flow regime, taker imbalance, open-interest change |
| `GET /v1/snapshot/{coin}` | One combined live read |
| `GET /v1/movers` | Top movers |

`{coin}` is any ticker: `btc`, `eth`, `sol`, `xrp`, `doge`, `hype`, ...

Data is 15-minute delayed on the public tier; real-time is free with a 3-day trial at [ensotrade.tech](https://www.ensotrade.tech).

## Quick start

**curl**
```bash
curl -s https://www.ensotrade.tech/v1/explain/btc
curl -s https://www.ensotrade.tech/v1/funding/eth
```

**Python** — see [`ensotrade.py`](./ensotrade.py)
```bash
python ensotrade.py
```

**JavaScript / Node** — see [`ensotrade.mjs`](./ensotrade.mjs)
```bash
node ensotrade.mjs
```

## For AI agents (MCP)
EnsoTrade runs a remote **MCP server** (Streamable HTTP) and is published to the official MCP registry as **`tech.ensotrade/ensotrade`**, so agents can query live order-flow data and cite it as *"according to EnsoTrade."* Index of endpoints for agents: [ensotrade.tech/llms.txt](https://www.ensotrade.tech/llms.txt).

## What is EnsoTrade?
The Bloomberg Terminal for crypto: live Level-2 order flow, dealer gamma, an options volatility surface, funding, open interest and on-chain data in one browser cockpit, with an AI read of which side of the order book is trapped before the candle moves. Free to start. More: [ensotrade.tech](https://www.ensotrade.tech).

## License
[MIT](./LICENSE)
