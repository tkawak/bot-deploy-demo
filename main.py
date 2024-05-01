import time

import requests


def main():
    while True:
        # r = requests.get("https://api.coin.z.com/public//v1/ticker?symbol=BTC")
        # r = requests.get("https://api.coin.z.com/public/v1/status")
        r = requests.get("https://api.bitflyer.com/v1/getticker?product_code=ETH_JPY")
        data = r.json()
        print(data)

        time.sleep(1.0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
