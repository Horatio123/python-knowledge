import _socket
import math

import requests
import urllib3

if __name__ == '__main__':
    res = requests.get(url='https://gw.alipayobjects.com/os/alisis/geo-data-v0.1.1/administrative-data/area-list.json')
    print(res.text)

    print(_socket.__file__)
    print(math.__file__)
    print(requests.__file__)
    print(urllib3.__file__)

