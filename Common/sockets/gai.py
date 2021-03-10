import socket


def gai(address):
    try:
        for res in socket.getaddrinfo(address, None, proto=socket.IPPROTO_TCP):
            family = res[0]
            sockaddr = res[4]
            print(family, sockaddr)
    except socket.gaierror:
        print('Invalid')


if __name__ == '__main__':
    gai('www.google.com')
    # IPv4 in hex
    gai('0xc000027b')
    # IPv4 in decimal
    gai('3221226198')
