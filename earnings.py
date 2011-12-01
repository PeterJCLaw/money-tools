#!/usr/bin/env python

import sys
from rates import orderedRates, income_tax

def earningsFromTax(rates, tax):
	if tax == 0:
		return "Up to %s" % rates[0]

	earn = 0

	for (rate, level) in orderedRates(rates):
		max_tax = level * rate	# at this band

#		print rate, level, max_tax, tax

		if tax > max_tax:
			tax -= max_tax
			earn += level
		else:	# they're in this band
			earn += tax / rate
			break

	return earn

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage: earnings TAX'
		exit(1)
	print earningsFromTax(income_tax, int(sys.argv[1]))
