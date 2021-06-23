# Currency exchange rates statistics

A console Python program that fetches
echange rates from https://exchangerate.host/#/ and counts statistical data
written as part of the recruitment process for shorte.st.

## Installation

After cloning create virtual enviroment (optional) and install dependencies.
Linux

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

Windows

    $ virtualenv venv
    $ venv\Scripts\activate
    (venv) $ pip install -r requirements.txt

## Running

### Example input

`./currency_stats.py EUR USD 2021-01-01 2021-05-02`

### Example output

`{"currency": "EUR/USD", "avg": 1.2, "med": 1.21, "75p": 1.21, "95p": 1.22}`

## Tests

To run a tests type: `pytest`
