#!/usr/bin/env python3

import numpy
import requests
import datetime


def __reduce_exchange_rates(exchange_rates: numpy.array, reducer):
    try:

        if numpy.any(exchange_rates < 0):
            raise Exception("Negative values are not allowed")

        if exchange_rates.ndim > 1:
            raise Exception("Multidimensional arrays are not allowed")

        if exchange_rates.size == 0:
            result = 0
        else:
            result = reducer(exchange_rates)

        return result
    except:
        return False


def count_exchange_rates_percentile(
    exchange_rates: numpy.array, percentile: int): return __reduce_exchange_rates(exchange_rates, lambda exchange_rates: numpy.percentile(exchange_rates, percentile))


def count_exchange_rates_median(
    exchange_rates): return __reduce_exchange_rates(exchange_rates, numpy.median)


def count_exchange_rates_mean(
    exchange_rates): return __reduce_exchange_rates(exchange_rates, numpy.mean)


def is_valid_date(datestring):
    try:
        year, month, day = datestring.split('-')
        datetime.datetime(int(year), int(month), int(day))
        return True
    except Exception:
        return False


def get_available_currencies():
    try:
        url = 'https://api.exchangerate.host/symbols'
        response = requests.get(url)
        data = response.json()
        if(data['success']):
            return data['symbols'].keys()
        else:
            raise Exception("Symbols couldn't be loaded")
    except:
        return []


def get_exchange_rates(selling_currency: str, buying_currency: str, date_start: str, date_end: str):
    try:

        if(not type(selling_currency) == str):
            raise Exception("selling_currency must be an str")

        if(not type(buying_currency) == str):
            raise Exception("buying_currency must be an str")

        if(not type(date_start) == str):
            raise Exception("date_start must be an str")

        if(not is_valid_date(date_start)):
            raise Exception("date_start is not valid")

        if(not type(date_end) == str):
            raise Exception("date_end must be an str")

        if(not is_valid_date(date_end)):
            raise Exception("date_end is not valid")

        available_currencies = get_available_currencies()

        if(not selling_currency in available_currencies):
            raise Exception("Selling currency symbol is incorrect")

        if(not buying_currency in available_currencies):
            raise Exception("Buying currency symbol is incorrect")

        url = 'https://api.exchangerate.host/timeseries?base={}&symbols={}&start_date={}&end_date={}'.format(
            selling_currency, buying_currency, date_start, date_end)
        response = requests.get(url)
        data = response.json()

        if(data['success']):
            exchange_rates = numpy.array([])
            for date, rates in data['rates'].items():
                numpy.append(exchange_rates, rates[buying_currency])
            return exchange_rates
        else:
            raise Exception("Exchange rates couldn't be loaded")
    except Exception as e:
        print(e)
        return False


def main():
    print('Hello world!')


if __name__ == "__main__":
    main()
