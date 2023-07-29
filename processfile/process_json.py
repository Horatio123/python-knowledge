import json


def dump_json():
    print("dump str-----------------------")
    content = {"name":"肯尼亚","level":"country","adcode":"肯尼亚","lng":37.86169142636884,"lat":0.534299750273016,"childrenNum":0,"parent":"null"}
    res = json.dumps(obj=content)
    print(type(res))
    print(res)

    print("dump file-----------------------")
    with open(file="country.json", mode="w") as f:
        json.dump(obj=content, fp=f, ensure_ascii=False)


def read_json():
    print("read str----------------------------")
    content = '{"name":"肯尼亚","level":"country","adcode":"肯尼亚","lng":37.86169142636884,"lat":0.534299750273016,"childrenNum":0,"parent":"null"}'
    content_dict = json.loads(content)
    print(type(content))
    print(type(content_dict))
    print(content_dict.get('name'))

    print("read file--------------------------")
    with open(file="country.json", mode="r") as fr:
        res = json.load(fp=fr)
    print(type(res))
    print(res)
    print(res.get('name'))


if __name__ == '__main__':
    dump_json()
    read_json()
