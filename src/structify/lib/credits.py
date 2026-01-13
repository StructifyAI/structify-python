from __future__ import annotations

from typing import NewType

Credits = NewType("Credits", int)
USDollars = NewType("USDollars", float)

CREDITS_PER_CENT = 1000
CENTS_PER_DOLLAR = 100
CREDITS_PER_DOLLAR = CREDITS_PER_CENT * CENTS_PER_DOLLAR


def usd_to_credits(usd: USDollars) -> Credits:
    return Credits(round(float(usd) * CREDITS_PER_DOLLAR))


def credits_to_usd(credits: Credits) -> USDollars:
    return USDollars(float(credits) / CREDITS_PER_DOLLAR)
