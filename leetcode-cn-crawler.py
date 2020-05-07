import requests
import time

requests.packages.urllib3.disable_warnings()  # 为了避免弹出一万个warning，which is caused by 非验证的get请求
leetcode_url = 'https://leetcode-cn.com/'
sign_in_url = 'https://leetcode-cn.com/accounts/login/'
submissions_url = 'https://leetcode-cn.com/submissions/'

sleep_time = 5
USERNAME = "YourUsernamePlease"
PASSWORD = "YourPasswordPlease"


def login(username, password):
    client = requests.session()
    client.encoding = "utf-8"

    client.get(sign_in_url, verify=False)
    login_data = {'login': username, 'password': password}
    result = client.post(sign_in_url, data=login_data, headers=dict(Referer=sign_in_url))

    if result.ok:
        print("Login Successfully!")
    else:
        print("Login Failed!")
    return client


if __name__ == '__main__':
    client = login(USERNAME, PASSWORD)
