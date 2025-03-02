from tinydb import TinyDB
import json

# 创建或连接数据库
db = TinyDB('tinyDB/db_load.json')

# 假设你的JSON文件名为data.json
with open('tinyDB/result_list.json', 'r') as file:
    # 加载JSON文件内容
    data_to_insert = json.load(file)

# 插入数据到TinyDB
if isinstance(data_to_insert, list):
    db.insert_multiple(data_to_insert)
else:
    # 如果JSON文件包含单个对象而非数组，则直接插入
    db.insert(data_to_insert)

print("Data from JSON file inserted successfully.")