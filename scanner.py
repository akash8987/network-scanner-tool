import socket

def scan_port(host, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


def run():
    host = "127.0.0.1"
    ports = [22, 80, 443]

    for port in ports:
        scan_port(host, port)


if __name__ == "__main__":
    run()
