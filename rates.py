
import sys

INCOME_TAX = {
    7475: 0,
    35000: 0.2,
    150000: 0.4,
    sys.maxint: 0.5,
}

NATIONAL_INSURANCE = {
    7228: 0,
    42484: 0.12,
    sys.maxint: 0.02,
}

def ordered_rates(rates):
    return sorted(rates.items())
