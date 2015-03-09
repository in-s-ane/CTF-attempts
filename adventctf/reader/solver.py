import socket

HOST = "adctf2014.katsudon.org"
PORT = 43010

def prettyhex(inputstring):
    outputhex = ""
    for char in inputstring:       
        outputhex += "\\x" + char.encode('hex')
    return outputhex

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    barcode = sock.recv(1024)
    barcode += sock.recv(1024)
    print barcode
    print prettyhex(barcode)

main()
