// Minimal client for the EnsoTrade live crypto order-flow API (https://www.ensotrade.tech/v1)
const BASE = "https://www.ensotrade.tech/v1";

const get = async (path) =>
  (await fetch(BASE + path, { headers: { "User-Agent": "ensotrade-api-example" } })).json();

export const explain = (coin) => get(`/explain/${coin}`);   // why a coin is up or down
export const funding = (coin) => get(`/funding/${coin}`);   // funding, crowding, OI, basis
export const orderflow = (coin) => get(`/orderflow/${coin}`); // regime, taker imbalance, OI change

// Demo (run: node ensotrade.mjs)
if (import.meta.url === `file://${process.argv[1]}`) {
  const coin = "btc";
  console.log("WHY:       ", (await explain(coin)).summary);
  console.log("FUNDING:   ", (await funding(coin)).summary);
  console.log("ORDER FLOW:", (await orderflow(coin)).summary);
}
