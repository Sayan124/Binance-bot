import os
import argparse
from pprint import pprint
from client import create_client
from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.stop_limit import stop_limit_order
from advanced.twap import twap_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Bot")

    parser.add_argument("symbol")
    parser.add_argument("side")
    parser.add_argument("type", choices=["market", "limit", "stop", "twap"])
    parser.add_argument("qty", type=float)

    parser.add_argument("--price", type=float)
    parser.add_argument("--stop", type=float)
    parser.add_argument("--parts", type=int)
    parser.add_argument("--delay", type=int)

    args = parser.parse_args()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_sec = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_sec:
      raise Exception("❌ Binance API keys not found in environment variables")

    client = create_client(api_key, api_sec)

    if args.type == "market":
        order = place_market_order(client, args.symbol, args.side, args.qty)
        
        if order:
          print("✅ Order placed successfully")
          pprint(order)
        else:
          print("❌ Order failed. Check bot.log for details.")

    elif args.type == "limit":
        order = place_limit_order(client, args.symbol, args.side, args.qty, args.price)
        
        if order:
          print("✅ Order placed successfully")
          pprint(order)
        else:
          print("❌ Order failed. Check bot.log for details.")

    elif args.type == "stop":
        order = stop_limit_order(client, args.symbol, args.side, args.qty, args.stop, args.price)
        
        if order:
          pprint("✅ Order placed successfully")
          print(order)
        else:
          print("❌ Order failed. Check bot.log for details.")

    elif args.type == "twap":
        order = twap_order(client, args.symbol, args.side, args.qty, args.parts, args.delay)
        if order:
          print("✅ Order placed successfully")
          pprint(order)
        else:
          print("❌ Order failed. Check bot.log for details.")

if __name__ == "__main__":
  main()