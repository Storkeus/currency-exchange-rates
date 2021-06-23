# get_exchange_rates function testing

import pytest
import numpy
from currency_stats import get_exchange_rates


@pytest.fixture
def correct_date_start():
    return '2020-01-01'


@pytest.fixture
def correct_date_end():
    return '2021-04-30'


@pytest.fixture
def incorrect_date_value():
    return '2020-01-0a'


@pytest.fixture
def incorrect_date_format():
    return '2020-01-0a'


@pytest.fixture
def correct_base_currency():
    return 'USD'


@pytest.fixture
def correct_target_currency():
    return 'EUR'


@pytest.fixture
def incorrect_currency():
    return 'XYZ1'


@pytest.fixture
def nonstring_value():
    return [1, 2, 3]


def test_nonstring_values(nonstring_value):
    assert(get_exchange_rates(nonstring_value,
           nonstring_value, nonstring_value,  nonstring_value) == False)


def test_incorrect_target_currency(incorrect_currency, correct_target_currency, correct_date_start,  correct_date_end):
    assert(get_exchange_rates(incorrect_currency,
           correct_target_currency, correct_date_start,  correct_date_end) == False)


def test_incorrect_base_currency(correct_base_currency, incorrect_currency,  correct_date_start,  correct_date_end):
    assert(get_exchange_rates(correct_base_currency, incorrect_currency,
           correct_date_start,  correct_date_end) == False)


def test_incorrect_date_start_value(correct_base_currency, correct_target_currency, incorrect_date_value, correct_date_end):
    assert(get_exchange_rates(correct_base_currency,
           correct_target_currency, incorrect_date_value, correct_date_end) == False)


def test_incorrect_date_end_value(correct_base_currency, correct_target_currency, correct_date_start, incorrect_date_value):
    assert(get_exchange_rates(correct_base_currency,
           correct_target_currency, correct_date_start, incorrect_date_value) == False)


def test_incorrect_date_end_format(correct_base_currency, correct_target_currency, correct_date_start, incorrect_date_format):
    assert(get_exchange_rates(correct_base_currency,
           correct_target_currency, correct_date_start, incorrect_date_format) == False)


def test_incorrect_date_start_format(correct_base_currency, correct_target_currency, incorrect_date_format, correct_date_end):
    assert(get_exchange_rates(correct_base_currency,
           correct_target_currency, incorrect_date_format, correct_date_end) == False)


def test_everything_correct(correct_base_currency, correct_target_currency, correct_date_start, correct_date_end):
    assert(type(get_exchange_rates(correct_base_currency, correct_target_currency,
           correct_date_start, correct_date_end)) == numpy.ndarray)
