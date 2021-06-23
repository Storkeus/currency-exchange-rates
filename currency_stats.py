#!/usr/bin/env python3

import json
from lib.calculations_on_exchange_rates import count_exchange_rates_mean, count_exchange_rates_median, count_exchange_rates_percentile
import numpy
from numpy.lib import percentile
import requests
import datetime
import sys
import argparse


def get_exchange_rates(currency_base: str, currency_target: str, date_start: str, date_end: str):
    def is_valid_date(datestring):
        try:
            year, month, day = datestring.split('-')
            datetime.datetime(int(year), int(month), int(day))
            return True
        except Exception:
            return False

    def get_available_currencies():
        try:
            # API endpoint that returns list of available symbols
            url = 'https://api.exchangerate.host/symbols'
            response = requests.get(url)
            data = response.json()
            if(data['success']):
                return data['symbols'].keys()
            else:
                raise Exception("Symbols couldn't be loaded")
        except:
            return []
    try:

        if(not type(currency_base) == str):
            raise Exception("currency_base must be an str")

        if(not type(currency_target) == str):
            raise Exception("currency_target must be an str")

        if(not type(date_start) == str):
            raise Exception("date_start must be an str")

        if(not is_valid_date(date_start)):
            raise Exception("date_start is not valid")

        if(not type(date_end) == str):
            raise Exception("date_end must be an str")

        if(not is_valid_date(date_end)):
            raise Exception("date_end is not valid")

        available_currencies = get_available_currencies()

        if(not currency_base in available_currencies):
            raise Exception("Selling currency symbol is incorrect")

        if(not currency_target in available_currencies):
            raise Exception("Buying currency symbol is incorrect")

        # API endpoint that returns exchange rates in given time
        url = 'https://api.exchangerate.host/timeseries?base={}&symbols={}&start_date={}&end_date={}'.format(
            currency_base, currency_target, date_start, date_end)

        response = requests.get(url)
        data = response.json()

        if(data['success']):
            rates = data['rates'].items()
            exchange_rates = numpy.empty(len(rates))
            i = 0
            for date, rates in rates:
                exchange_rates[i] = rates[currency_target]
                i += 1
            return exchange_rates
        else:
            raise Exception("Exchange rates couldn't be loaded")
    except Exception as e:
        print(e)
        return False


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
