from __future__ import annotations

import collections
import csv
import datetime
from decimal import Decimal
from typing import Mapping

import dateutil.parser


def parse_line(mapping: dict[str, str]) -> tuple[datetime.date, Decimal]:
    """
    Parse a line from the Bank of England base rate CSV.
    """
    return (
        dateutil.parser.parse(mapping['Date Changed']).date(),
        Decimal(mapping['Rate']) / 100,
    )


def with_interest(principal, aer, th_of_year=1):
    """
    Given an AER and the fraction of a year over which interest is applied (e.g:
    th_of_year=12 is monthly), compute the actual interest over a single step of
    that time-window.

    For example, to compute one month's worth of a monthly applied AER of 5% on
    £100:
        >>> with_interest(100, .05, 12)
        Decimal('100.4081740038578570206570506')
    """

    th_of_year = Decimal(th_of_year)
    annual_mult = 1 + Decimal(aer)
    incremental_mult = annual_mult ** (1 / th_of_year)
    incremental_rate = incremental_mult - 1

    return principal * (1 + incremental_rate / th_of_year) ** th_of_year


def annualised_with_interest(principal, aer, times_per_year=1):
    """
    Given an AER and the fraction of a year over which interest is applied (e.g:
    times_per_year=12 is monthly), compute the actual compoound interest over a
    year.

    This exists mostly to validate `with_interest` -- it should always return
    the same value as applying the AER directly. For this reason the result is
    quantised before being returned.

        >>> annualised_with_interest(100, .05, 12)
        Decimal('101.00')
    """
    value = principal
    for _ in range(times_per_year):
        value = with_interest(value, aer, th_of_year=times_per_year)
    return value.quantize(Decimal('0.01'))


def iterdays(start: datetime.date, end: datetime.date):
    now = start
    while now < end:
        yield now
        now += datetime.timedelta(days=1)


def itermonths(start: datetime.date, end: datetime.date):
    this_month = None
    for day in iterdays(start, end):
        if day.month != this_month:
            yield day
            this_month = day.month


def rate_at(
    rate_changes: Mapping[datetime.date, Decimal],
    now: datetime.date,
) -> Decimal:
    """
    Given a mapping of times at which the interest rate changed and the new
    value introduced at that date, return the rate on a given date.
    """
    rate = None
    for date, new_rate in sorted(rate_changes.items()):
        if date > now:
            break
        rate = new_rate
    if rate is None:
        raise ValueError(f"No rates for {now}!")
    return rate


def compute(
    start: datetime.date,
    end: datetime.date,
    rates: Mapping[datetime.date, Decimal],
    principal: int | Decimal = 100,
) -> Decimal:
    """
    Compute the result of applying a changing interest rate on a principal over
    time.

    While the rates may change at any time, interest is computed monthly using
    the rate value from the first of the month. For interest calculations,
    months are assumed to evenly split the year.

    The result is quantised only at the end, not between adding interest.
    """
    value = Decimal(principal)
    for month in itermonths(start, end):
        rate = rate_at(rates, month)
        value = with_interest(value, rate, th_of_year=12)
    return value.quantize(Decimal('0.01'))


with open('Downloads/Bank Rate history and data Bank of England Database.csv') as f:
    reader = csv.DictReader(f)
    bank_of_england_rates = collections.OrderedDict(
        reversed([parse_line(x) for x in reader]),
    )
