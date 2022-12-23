#!/usr/bin/env python

import sys
from rates import ordered_rates, INCOME_TAX

def earnings_from_tax(rates, tax):
    if tax == 0:
        return f"Up to {rates[0]}"

    earn = 0

    for (rate, level) in ordered_rates(rates):
        max_tax = level * rate	# at this band

        if tax > max_tax:
            tax -= max_tax
            earn += level
        else:	# they're in this band
            earn += tax / rate
            break

    return earn

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: earnings TAX")
        exit(1)
    print(earnings_from_tax(INCOME_TAX, int(sys.argv[1])))
