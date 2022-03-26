
import sys

INCOME_TAX = {
    12570: 0,
    50270: 0.2,
    150000: 0.4,
    sys.maxint: 0.5,
}

NATIONAL_INSURANCE = {
    9564: 0,
    50268: 0.12,
    sys.maxint: 0.02,
}

def ordered_rates(rates):
    return sorted(rates.items())
