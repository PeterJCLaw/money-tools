#!/usr/bin/env python

import sys
from tax import tax_from_earnings
from rates import NATIONAL_INSURANCE

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ni EARNINGS")
        exit(1)
    print(tax_from_earnings(NATIONAL_INSURANCE, int(sys.argv[1])))
