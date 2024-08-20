import socket
from time import sleep


def socket_client_send_list():
    HOST = "192.168.0.116"  # The server's hostname or IP address
    PORT = 6000  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        cmds = [b"$010F040014#", b"$010F040115#", b"$01100800000019#", b"$01100804ce00eb#"]
        for cmd in cmds:
            s.sendall(cmd)
            print(f'send {cmd}')
            # data = s.recv(1024)
            # print(f'receive {data}')
            sleep(0.2)

        # s.sendall(b"$010F040014#")
        # print(f"send Hello world")
        # data = s.recv(1024)
        # print(f"Received {data!r}")
        # s.sendall(b"$010F040115#")
        # data2 = s.recv(1024)
        # print(f"Received {data2!r}")

        while True:
            sleep(0.5)
            s.sendall(b"$01100804ce00eb#")
            print(f'send b"$01100804ce00eb#"')
            # data = s.recv(1024)
            # print(f'receive {data}')

            print('working')


def socket_client():
    HOST = "192.168.0.116"  # The server's hostname or IP address
    PORT = 6000  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # cmd = b"$01100804e70004#"
        cmd = b"$01100800000019#"
        s.sendall(cmd)
        print(f"send {cmd}")
        data = s.recv(1024)
        print(f"Received {data!r}")
        # s.sendall(b"$010F040115#")
        # data2 = s.recv(1024)
        # print(f"Received {data2!r}")


if __name__ == '__main__':
    # socket_client()
    socket_client_send_list()
