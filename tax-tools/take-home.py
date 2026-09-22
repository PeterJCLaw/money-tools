#!/usr/bin/env python3

import sys
from decimal import Decimal

from rates import INCOME_TAX, NATIONAL_INSURANCE
from tax import tax_from_earnings


def quantize_gbp(value: Decimal) -> Decimal:
    return value.quantize(Decimal('0.01'))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: take-home EARNINGS")
        exit(1)

    earnings = int(sys.argv[1])
    tax = tax_from_earnings(INCOME_TAX, earnings)
    ni = tax_from_earnings(NATIONAL_INSURANCE, earnings)
    print(f"Tax: {quantize_gbp(tax):>10}")
    print(f"NI:  {quantize_gbp(ni):>10}")
    print(f"Take:{quantize_gbp(earnings - tax - ni):>10}")
