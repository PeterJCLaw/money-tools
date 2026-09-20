#!/usr/bin/env python3

import sys

from rates import NATIONAL_INSURANCE
from tax import tax_from_earnings

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ni EARNINGS")
        exit(1)
    print(tax_from_earnings(NATIONAL_INSURANCE, int(sys.argv[1])))
