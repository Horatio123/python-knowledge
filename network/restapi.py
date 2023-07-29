import _socket
import math

import requests
import urllib3
from urllib3 import encode_multipart_formdata


def upload_oss_zip(p):
    del p['host']
    with open('xxx.zip', 'rb') as f:
        p.update({"file": f.read()})
        encode_data = encode_multipart_formdata(p)
        file_data = encode_data[0]
        header = {'Content-Type': encode_data[1]}
        result = requests.post(url='https://xxxxxx.oss-cn-hangzhou.aliyuncs.com', headers=header, data=file_data)
    print(result.text)


if __name__ == '__main__':
    res = requests.get(url='https://gw.alipayobjects.com/os/alisis/geo-data-v0.1.1/administrative-data/area-list.json')
    print(res.text)

    print(_socket.__file__)
    print(math.__file__)
    print(requests.__file__)
    print(urllib3.__file__)

