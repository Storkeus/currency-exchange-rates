# count_exchange_rates_percentile function testing

from lib.calculations_on_exchange_rates import count_exchange_rates_percentile
import numpy


def test_empty_list():
    exchange_rates = numpy.array([])
    assert(count_exchange_rates_percentile(exchange_rates, 75) == 0)


def test_single_value():
    exchange_rates = numpy.array([5])
    assert(count_exchange_rates_percentile(exchange_rates, 75) == 5)


def test_multiple_values():
    exchange_rates = numpy.array([5, 5.3, 1.2, 4.7])
    assert(count_exchange_rates_percentile(exchange_rates, 75) == 5.075)


def test_multiple_values():
    exchange_rates = numpy.array([5, 5.3, 1.2, 4.7])
    assert(count_exchange_rates_percentile(exchange_rates, 95) == 5.255)


def test_negative_values():
    exchange_rates = numpy.array([-5, 5.3, 1.2, 4.7])
    assert(count_exchange_rates_percentile(exchange_rates, 75) == False)


def test_non_numeric_values():
    exchange_rates = numpy.array([5, 'aaa', 1.2, 4.7])
    assert(count_exchange_rates_percentile(exchange_rates, 75) == False)


def test_multiple_dimension():
    exchange_rates = numpy.array([[5, 1.2, 4.7], [5, 1.2, 4.7]])
    assert(count_exchange_rates_percentile(exchange_rates, 75) == False)


def test_too_large_percentile():
    exchange_rates = numpy.array([[5, 1.2, 4.7]])
    assert(count_exchange_rates_percentile(exchange_rates, 105) == False)


def test_too_small_percentile():
    exchange_rates = numpy.array([[5, 1.2, 4.7]])
    assert(count_exchange_rates_percentile(exchange_rates, -10) == False)
