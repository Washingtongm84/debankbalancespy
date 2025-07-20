import requests
import os
from typing import List

DEBANK_BASE_URL = "https://pro-openapi.debank.com/v1/user/total_balance"
DEBANK_ACCESS_KEY = os.getenv("DEBANK_ACCESS_KEY")

def get_balance(address: str) -> dict:
    headers = {
        "accept": "application/json",
        "AccessKey": DEBANK_ACCESS_KEY
    }
    params = {
        "id": address
    }
    resp = requests.get(DEBANK_BASE_URL, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

def batch_check_balances(addresses: List[str]):
    print("Address,Balance (USD)")
    for addr in addresses:
        try:
            data = get_balance(addr)
            print(f"{addr},{data.get('total_usd_value', 0):.2f}")
        except Exception as e:
            print(f"{addr},ERROR ({e})")

if __name__ == "__main__":
    filename = input("Введите путь к файлу с адресами: ").strip()
    with open(filename, "r") as f:
        addresses = [line.strip() for line in f if line.strip()]
    batch_check_balances(addresses)