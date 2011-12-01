#!/usr/bin/env python

import sys
from rates import income_tax, orderedRates

def taxFromEarnings(rates, earn):
	tax = 0

	for (rate, level) in orderedRates(rates):
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
		print 'Usage: tax EARNINGS'
		exit(1)
	print taxFromEarnings(income_tax, int(sys.argv[1]))
