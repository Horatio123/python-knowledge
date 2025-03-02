from tinydb import TinyDB, Query
import json
# 创建或连接数据库文件
db = TinyDB('tinyDB/db.json')

# 插入数据
db.insert({'name': 'Alice', 'age': 25, 'city': 'New York'})
db.insert({'name': 'Bob', 'age': 30, 'city': 'San Francisco'})

# 查询数据
User = Query()
results = db.search(User.city == 'New York')
print("People in New York:")
for item in results:
    print(item)

# 更新数据
db.update({'age': 26, 'old': True}, User.name == 'Alice')

# 删除数据
db.remove(User.age >= 70)

# 显示所有数据
print("\nAll people:")
all_results = db.all()
all_results_list = []
for item in all_results:
    print(item)
    all_results_list.append(item)

with open(file="tinyDB/result_list.json", mode="w") as f:
    json.dump(fp=f, obj=all_results_list)

# 关闭数据库（可选）
db.close()