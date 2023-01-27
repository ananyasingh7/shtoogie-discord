import requests


class StockService:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url_base = "https://www.alphavantage.co/"

    def get_stock_info(self, symbol, fullInfo: bool):
        url = f"{self.url_base}/query/?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            if fullInfo:
                return data
            else:
                price = data["Global Quote"]["05. price"]
                return price
        except (requests.ConnectionError, requests.HTTPError, requests.Timeout) as e:
            print(e)
            return e
