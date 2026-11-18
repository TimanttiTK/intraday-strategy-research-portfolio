# Research methodology and limits

## Evaluation approach

- Compare London-session and New York-session systems as separate strategies.
- Use 15-minute OHLCV candles and explicit session-local time handling.
- Model the signal at candle close and the market entry at a following candle open where applicable.
- Include the configured per-side commission in the reported simulations.
- Track trades, win rate, net return, profit factor where available, and peak-to-trough drawdown.
- Visually inspect executions to catch mismatches between written rules and chart behavior.

## Limits

- The public repository does not include raw candles or individual trade exports, so the reported snapshot cannot be reproduced from this repository alone.
- The reported strategies were iterated using historical samples. Parameter selection creates a risk of overfitting and selection bias.
- The simplified models do not fully capture slippage, funding, queue priority, partial fills, or operational delays.
- Binance historical tests and Hyperliquid live monitoring use different venue data and execution conditions.
- Historical performance does not predict future performance.

The strategy source remains private; this document describes the review process without publishing exact thresholds or trading signals.
