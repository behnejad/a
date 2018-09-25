import requests


def makeRequest(method: str) -> requests.request:
    method = method.lower()

    if method == 'post':
        return requests.post
    elif method == 'get':
        return requests.get
    elif method == 'put':
        return requests.put
    elif method == 'delete':
        return requests.delete
