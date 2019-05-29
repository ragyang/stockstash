import requests
import json

def get_TIME_SERIES_DAILY(ticker):
    """Calls the Alpha Vantage TIME_SERIES_DAILY API to get time series daily

    Params:
        1) ticker
            type: string
            desc: stock symbol
    Return Value:
        json response from the API call
    
    API Documentation:
        https://www.alphavantage.co/documentation/
    """
    apikey = 'W6Y6NLWDMM2FVX9B'
    fullurl = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=" + apikey
    r = requests.get(fullurl)
    r_json = json.loads(r.text)
    return r_json

def is_valid_ticker(ticker):
    """Checks if a given ticker/symbol is valid

    Params:
        1) ticker
            type: string
            desc: stock symbol

    Return Value:
        boolean - true if valid ticker, false otherwise
    """
    response = get_TIME_SERIES_DAILY(ticker)
    if response.get('Error Message') is None:
        return True
    return False