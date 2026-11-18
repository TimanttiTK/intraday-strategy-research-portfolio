# Architecture overview

## Processing flow

1. Read candle data from the selected venue.
2. Normalize timestamps, candle intervals, and session-local clocks.
3. Build session context and opening-range levels.
4. Pass context into a private signal module.
5. Simulate fills, stops, fees, and risk limits.
6. Record trades and calculate performance metrics.
7. Inspect each trade on a visual chart and compare the backtest with live, read-only alerts.

## Separation of concerns

- **Data adapters** supply historical or live candles without embedding account credentials.
- **Signal modules** define the strategy-specific entry and exit conditions; these remain private.
- **Simulation** applies position sizing, fees, stop handling, and portfolio accounting.
- **Review tools** expose trades and metrics so individual entries and exits can be audited.
- **Alert monitoring** reads public live candles and emits notifications only; it does not submit orders.

This separation made it possible to compare strategy changes without confusing data-source differences with rule changes. Binance was used for the historical comparison; the local monitoring adapters use Hyperliquid public candles, so live alerts can differ from historical test signals.
