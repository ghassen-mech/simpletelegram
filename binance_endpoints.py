from dotenv import load_dotenv
import os
from binance.client import Client
load_dotenv()
apiKey = os.getenv("APIKEY")
apiSecurity = os.getenv("APISECURITY")



class PrivateBinanceEndpoints:
    def __init__(self):
        self.client = Client(apiKey, apiSecurity)

    def get_balance(self):
        fiat_currency = 'USDT'
        account_info = self.client.get_account()
        exchange_info = self.client.get_exchange_info()
        trading_pairs = [symbol['symbol'] for symbol in exchange_info['symbols']]
        balances = account_info['balances']
        total_balance = 0
        for balance in balances:
            asset = balance['asset']
            free = float(balance['free'])
            locked = float(balance['locked'])

            trading_pair = f"{asset}{fiat_currency}"

            if trading_pair in trading_pairs:
                ticker = self.client.get_symbol_ticker(symbol=trading_pair)
                current_price = float(ticker['price'])
                estimated_balance = (free + locked) * current_price
                total_balance += estimated_balance

        balance = self.client.get_asset_balance(asset='USDT')
        total_balance += float(balance['free'])
        return "Your Balance is : %s" % total_balance
    def get_all_orders(self):
        return self.client.get_all_orders()
    def get_one_order(self, symbol, orderId):
        return self.client.get_order(symbol=symbol, orderId=orderId)


#symboles = PrivateBinanceEndpoints().get_symbols()
#print(symboles)
#balance = PrivateBinanceEndpoints().get_balance()
#print(balance)
#get_all_orders=PrivateBinanceEndpoints().get_all_orders()
#get_one_order = PrivateBinanceEndpoints().get_one_order("BTCUSDT")
#print(get_one_order)

class PublicBinanceEndpoints:
    def __init__(self):
        self.client = Client()
    def get_symbols(self):
        return self.client.get_exchange_info()

#symboles = PublicBinanceEndpoints().get_symbols()
#print(symboles)