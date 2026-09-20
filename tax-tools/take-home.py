#!/usr/bin/env python3

import sys

from rates import INCOME_TAX, NATIONAL_INSURANCE
from tax import tax_from_earnings

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: take-home EARNINGS")
        exit(1)

    earnings = int(sys.argv[1])
    tax = tax_from_earnings(INCOME_TAX, earnings)
    ni = tax_from_earnings(NATIONAL_INSURANCE, earnings)
    print(earnings - tax - ni)
