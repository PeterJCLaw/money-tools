import itertools
from decimal import Decimal

INCOME_TAX = {
    12570: Decimal(0),
    50270: Decimal('0.2'),
    125470: Decimal('0.4'),
    float('inf'): Decimal('0.45'),
}

NATIONAL_INSURANCE = {
    12570: Decimal(0),
    50270: Decimal('0.08'),
    float('inf'): Decimal('0.02'),
}

INCOME_TAX_TAPER_THRESHOLD = 100_000


def ordered_rates(rates):
    for level in sorted(rates.keys()):
        yield rates[level], level


def ordered_bands(rates):
    for bottom, top in itertools.pairwise((0, *rates.keys())):
        yield rates[top], (bottom, top)
