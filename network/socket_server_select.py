import socket
import selectors
import types
from time import sleep

"""
https://realpython.com/python-sockets/#handling-multiple-connections
"""


def accept_wrapper(sock):
    print("go into accept_wrapper")
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
            print(f"get data: {recv_data}")
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]
        else:
            print("nothing to write")


def socket_server():

    host = '127.0.0.1'
    port = 1111
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((host, port))
    lsock.listen()
    print(f"Listening on {(host, port)}")
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)
    time = 1

    try:
        while True:
            print(f"----------------------enter true time {time}")
            # print(f"sel get map: {sel.get_map()}")
            time = time + 1
            events = sel.select(timeout=None)
            for key, mask in events:
                print(f'key is {key}')
                print(f'mask is {mask}')
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    service_connection(key, mask)
            sleep(3)
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        sel.close()


if __name__ == '__main__':
    sel = selectors.DefaultSelector()
    socket_server()
