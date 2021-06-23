#!/usr/bin/env python3

import json
from lib.get_exchange_rates import get_exchange_rates
from lib.calculations_on_exchange_rates import count_exchange_rates_mean, count_exchange_rates_median, count_exchange_rates_percentile
from numpy.lib import percentile
import sys
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='A program that returns mean, mediana, 75 percentil and 95 percentil of exchange rates for given currencies in given time')

    parser.add_argument('currency_base', metavar='currency_base',
                        help='Base currency for exchange rates')

    parser.add_argument('currency_target', metavar='currency_target',
                        help='Target currency for exchange rates')

    parser.add_argument('date_start', metavar='date_start',
                        help='Start date for exchange rates list')

    parser.add_argument('date_end', metavar='date_start',
                        help='End date for exchange rates list')

    arguments_raw = sys.argv
    # Remove file name from arguments as it is not needed
    del arguments_raw[0]
    arguments = parser.parse_args(sys.argv)

    # Get and process exchange rates
    exchange_rates = get_exchange_rates(
        arguments.currency_base, arguments.currency_target, arguments.date_start, arguments.date_end)

    result = dict()

    def format_result(result): return round(result, 2)
    mean = format_result(count_exchange_rates_mean(exchange_rates))
    median = format_result(count_exchange_rates_median(exchange_rates))
    percentile_75 = format_result(
        count_exchange_rates_percentile(exchange_rates, 75))
    percentile_95 = format_result(
        count_exchange_rates_percentile(exchange_rates, 95))

    result['currency'] = "{}/{}".format(arguments.currency_base,
                                        arguments.currency_target)

    result['avg'] = mean
    result['med'] = median
    result['75p'] = percentile_75
    result['95p'] = percentile_95
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    main()
