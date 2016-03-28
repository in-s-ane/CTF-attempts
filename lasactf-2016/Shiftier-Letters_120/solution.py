import string
import socket
import urllib2

alphabet = string.ascii_lowercase

def caesar(plaintext, shift):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

words = open("/usr/share/dict/words", "r").read().split("\n")
enc = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("web.lasactf.com", 4056))

def send(candidate):
    global sock
#     print "%s : %s" % (enc, candidate)
    try:
        sock.send(candidate)
    except:
        return

while "lasactf" not in enc:
    enc = sock.recv(1024)
    print enc
    solved = False
    candidate = ""
    if "Incorrect" in enc or "Ran out of time" in enc:
        break
    for x in range(26):
        candidate = caesar(enc, x)
        for word in candidate.split():
            if len(word) > 5 and word in words:
                solved = True
                send(candidate)
                break
        if solved:
            break
    print "========="


print enc
