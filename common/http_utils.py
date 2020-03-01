import requests

# header扩展如有需要自行扩展即可

def send_post_json(url,data):
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    json_body = data
    result = requests.post(url=url, headers=headers, data=json_body)
    return result.text

def send_post(urlParam):
    result = requests.post(url=urlParam)
    return result.text


def send_get(urlParam):
    result = requests.get(url=urlParam)
    return result.text


if __name__ == '__main__':
    url = 'http://localhost:8080/itest/post/json'
    json_body = '{"param1":1,"param2":2}'
    res = send_post_json(url, json_body)
    print(res)

    url = 'http://localhost:8080/itest/post/kv?param1=1&param2=2'
    res = send_post(url)
    print(res)

    url = 'http://localhost:8080/itest/get?param1=1&param2=2'
    res = send_get(url)
    print(res)

