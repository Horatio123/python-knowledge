import pymysql

db = pymysql.connect(
    host='xxxxx.mysql.rds.aliyuncs.com',
    user='aaaa',
    password='cccc',
    database='dddd')


def get_job_id(p_name, p_build_number):
    db = pymysql.connect(host='rm-xxx.mysql.rds.aliyuncs.com', user='tcd_adm', password='xxxx', database='ccccc')
    cursor = db.cursor()
    sql = f"""select id from cc where build_number = {p_build_number} and name = '{p_name}'"""
    cursor.execute(sql)
    res_job_id = 0
    try:
        res_job_id = cursor.fetchall()[0][0]
        print(f"get job_id is {res_job_id}")
    except Exception:
        print(f"ERROR: get job_id fail where name is {p_name} and build_name is {p_build_number}")
    return res_job_id


def get_data(p, s):
    cs = db.cursor()
    sql = "select * from job where build_number = %s and status = %s"
    param = (p, s)
    cs.execute(sql, param)
    data = cs.fetchall()
    print(data)


if __name__ == '__main__':
    get_data(4, 'FAILURE')
