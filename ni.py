#!/usr/bin/env python

import sys
from tax import taxFromEarnings
from rates import national_insurance

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ni EARNINGS'
        exit(1)
    print taxFromEarnings(national_insurance, int(sys.argv[1]))
