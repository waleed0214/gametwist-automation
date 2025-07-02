import requests

def get_api_balance(token):
    url = "https://www.gametwist.com/nrgs/de/api/userstate-v1"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["balance"]["funMoney"]
    return None
