import os
from binance.client import Client
from dotenv import load_dotenv
import logging

# Load .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Enable logging
logging.basicConfig(filename='bot.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Use Binance Futures Testnet URL
TESTNET_URL = "https://testnet.binancefuture.com"

client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = TESTNET_URL


def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market Order Success: {order}")
        print("Market Order Placed:", order)
    except Exception as e:
        logging.error(f"Market Order Error: {e}")
        print("Error:", e)


def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        logging.info(f"Limit Order Success: {order}")
        print("Limit Order Placed:", order)
    except Exception as e:
        logging.error(f"Limit Order Error: {e}")
        print("Error:", e)


# CLI Input
print("\n=== Simplified Trading Bot ===\n")

symbol = input("Enter symbol (example: BTCUSDT): ").upper()
side = input("Buy or Sell? (BUY/SELL): ").upper()
order_type = input("Order type (MARKET/LIMIT): ").upper()
quantity = float(input("Quantity: "))

if order_type == "MARKET":
    place_market_order(symbol, side, quantity)

elif order_type == "LIMIT":
    price = float(input("Limit Price: "))
    place_limit_order(symbol, side, quantity, price)

else:
    print("Invalid order type")