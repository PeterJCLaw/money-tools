#!/usr/bin/env python

import sys
from tax import tax_from_earnings
from rates import NATIONAL_INSURANCE, INCOME_TAX

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ni EARNINGS")
        exit(1)
    earnings = int(sys.argv[1])
    tax = tax_from_earnings(INCOME_TAX, earnings)
    ni = tax_from_earnings(NATIONAL_INSURANCE, earnings)
    print(earnings - tax - ni)
