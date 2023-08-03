import subprocess


class CustomException(Exception):
    pass


def execute_command(cmd, work_dir):
    result = ""
    process = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # 循环读取输出并打印
    while True:
        output = process.stdout.readline().decode()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip("\n"))
    # 获取返回码
    return_code = process.wait()
    if return_code != 0:
        raise CustomException(f"execute {cmd} is wrong")


if __name__ == '__main__':
    # execute_command('ls', '.')
    execute_command('cat shell_python.sh', '.')
