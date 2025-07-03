import requests

def get_api_token(username, password):
    url = "https://playerauthentication-at.greentube.com/gametwist.widgets.web.site/de/api/login-v1"
    payload = {
        "nickname": username,
        "password": password,
        "autoLogin": False
    }
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, json=payload, headers=headers)
   # print("Login status:", response.status_code)
   # print("Login response body:", response.text)
    if response.status_code == 200:
        return response.json().get("accessToken")
    return None
