"""Generic position-sizing illustration for the public research portfolio.

This example is not the production sizing code for the London or NYO systems.
It uses only an equity risk budget, a stop distance, and a notional cap.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PositionSize:
    quantity: float
    risk_budget: float
    estimated_stop_risk: float
    notional: float


def size_position(
    *,
    equity: float,
    risk_fraction: float,
    entry_price: float,
    stop_price: float,
    max_notional_multiple: float,
) -> PositionSize:
    """Return a generic quantity bounded by risk budget and notional exposure."""
    values = (equity, risk_fraction, entry_price, stop_price, max_notional_multiple)
    if any(value <= 0 for value in values):
        raise ValueError("All sizing inputs must be positive")

    stop_distance = abs(entry_price - stop_price)
    if stop_distance == 0:
        raise ValueError("Entry and stop prices must differ")

    risk_budget = equity * risk_fraction
    quantity_by_risk = risk_budget / stop_distance
    quantity_by_notional = equity * max_notional_multiple / entry_price
    quantity = min(quantity_by_risk, quantity_by_notional)
    notional = quantity * entry_price

    return PositionSize(
        quantity=quantity,
        risk_budget=risk_budget,
        estimated_stop_risk=quantity * stop_distance,
        notional=notional,
    )
