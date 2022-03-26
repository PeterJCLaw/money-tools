INCOME_TAX = {
    12570: 0,
    50270: 0.2,
    150000: 0.4,
    float('inf'): 0.5,
}

NATIONAL_INSURANCE = {
    9564: 0,
    50268: 0.12,
    float('inf'): 0.02,
}

def ordered_rates(rates):
    for level in sorted(rates.keys()):
        yield rates[level], level
