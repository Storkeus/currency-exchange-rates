import requests
import datetime
import numpy


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
