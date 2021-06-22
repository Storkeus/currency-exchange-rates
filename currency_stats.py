#!/usr/bin/env python3

import numpy


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


def count_exchange_rates_median(
    exchange_rates): return __reduce_exchange_rates(exchange_rates, numpy.median)


def count_exchange_rates_mean(
    exchange_rates): return __reduce_exchange_rates(exchange_rates, numpy.mean)


def main():
    print("Hello world!")


if __name__ == "__main__":
    main()
