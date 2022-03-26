#!/usr/bin/env python

import sys
from tax import taxFromEarnings
from rates import national_insurance, income_tax

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ni EARNINGS'
        exit(1)
    earnings = int(sys.argv[1])
    tax = taxFromEarnings(income_tax, earnings)
    ni = taxFromEarnings(national_insurance, earnings)
    print earnings - tax - ni
