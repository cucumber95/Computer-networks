import subprocess
import platform
import socket
import sys


def ping(host, size):
    if platform.system() == 'Windows':
        command = ["ping", "-n", "1", "-l", f"{size}", host]
    else:
        command = ["ping", "-c", "1", "-M", "do", "-s", f"{size}", host]
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    if result.returncode == 0:
        return True
    else:
        return False


def is_ip_valid(host):
    try:
        socket.inet_aton(host)
        return True
    except socket.error:
        return False


def is_host_available(host):
    return ping(host, 1)


def get_mtu(host):
    # get minimal MTU using binary search
    l = 1
    r = 2**16 + 1

    while r - l > 1:
        m = (l + r) / 2
        if ping(host, m):
            l = m
        else:
            r = m

    return r


def main():
    if len(sys.argv) != 2:
        print("Incorrect number of input arguments")
        sys.exit(1)

    host = sys.argv[1]
    if not is_ip_valid(host):
        print("Invalid host value")
        sys.exit(1)

    if not is_host_available(host):
        print("Host is not available or ICMP might be blocked")
        sys.exit(1)

    print(f"MTU for channel: {get_mtu(host)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Some exception occured: {e}")
        sys.exit(1)
