# import necessary py modules
import requests
from datetime import datetime

# function to fetch and convert the currency 
def convert_currency_fixerapi_free(src, dst, amount):
    url = f"http://data.fixer.io/api/latest?access_key=8c3dce10dc5fdb6ec1f555a1504b1373&symbols={src},{dst}&format=1"
    data = requests.get(url).json()
    if data["success"]:
        # request successful
        rates = data["rates"]
        # since we have the rate for our currency to src and dst, we can get exchange rate between both using below calculation
        exchange_rate = 1 / rates[src] * rates[dst]
        last_updated_datetime = datetime.fromtimestamp(data["timestamp"])
        return last_updated_datetime, exchange_rate * amount
    
if __name__ == "__main__":
    # get user input
    source_currency = input("\nEnter `Source Country` Currency Code: ")
    destination_currency = input("Enter `Destination Country` Currency Code: ")
    amount = float(input("Enter the Amount to convert: "))
    last_updated_datetime, exchange_rate = convert_currency_fixerapi_free(source_currency, destination_currency, amount)
    print("\nLast updated datetime:", last_updated_datetime)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}\n")
    