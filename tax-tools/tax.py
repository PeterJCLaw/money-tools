#!/usr/bin/env python

import sys
from rates import INCOME_TAX, ordered_rates

def tax_from_earnings(rates, earn):
    tax = 0

    for (rate, level) in ordered_rates(rates):
        left = earn - level
        if left > 0:
            earn = left
            tax += level * rate
        else:	# they're in this band
            tax += earn * rate
            break

    return tax

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: tax EARNINGS")
        exit(1)
    print(tax_from_earnings(INCOME_TAX, int(sys.argv[1])))
