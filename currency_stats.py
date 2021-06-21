#!/usr/bin/env python3

import numpy


def count_exchange_rates_mean(exchange_rates: numpy.array):
    try:

        if exchange_rates.size == 0:
            return 0

        if numpy.any(exchange_rates < 0):
            raise Exception("Negative values are not allowed")

        if exchange_rates.ndim > 1:
            raise Exception("Multidimensional arrays are not allowed")

        return numpy.mean(exchange_rates)
    except:
        return False


def main():
    print("Hello world!")


if __name__ == "__main__":
    main()
