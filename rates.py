
import sys

income_tax = {
    7475: 0,
    35000: 0.2,
    150000: 0.4,
    sys.maxint: 0.5,
}

national_insurance = {
    7228: 0,
    42484: 0.12,
    sys.maxint: 0.02,
}

def orderedRates(rates):
    keys = rates.keys()
    keys.sort()

    for level in keys:
        rate = rates[level]
        yield rate, level
