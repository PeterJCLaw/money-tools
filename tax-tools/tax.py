#!/usr/bin/env python3

import sys

from rates import INCOME_TAX, INCOME_TAX_TAPER_THRESHOLD, ordered_rates


def taper_rates(rates, earn, taper_threshold):
    allowance_loss = max(earn - taper_threshold, 0) // 2
    allowance_loss = min(allowance_loss, *rates.keys())

    def adjust_threshold(rate_threshold):
        if rate_threshold < taper_threshold:
            return rate_threshold - allowance_loss
        return rate_threshold

    return {adjust_threshold(k): v for k, v in rates.items()}


def tax_from_earnings(rates, earn):
    tax = 0

    for (rate, level) in ordered_rates(rates):
        left = earn - level
        if left > 0:
            earn = left
            tax += level * rate
        else:  # they're in this band
            tax += earn * rate
            break

    return tax


def tapered_tax_from_earnings(rates, earn, taper_threshold=INCOME_TAX_TAPER_THRESHOLD):
    return tax_from_earnings(
        taper_rates(rates, earn, taper_threshold),
        earn,
    )


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: tax EARNINGS")
        exit(1)

    print(tapered_tax_from_earnings(INCOME_TAX, int(sys.argv[1])))
