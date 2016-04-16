import hashlib

# Known header bytes
header = "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52"

enc = open("flag.encrypted", "rb").read().strip()
key = ""
for x in range(16):
    key += chr(ord(enc[x]) ^ ord(header[x]))

print "The key is %s" % key

dec = ""
for x in range(len(enc)):
    dec += chr(ord(enc[x]) ^ ord(key[x % len(key)]))

open("flag.png", "w").write(dec)

# Decompiling the apk, we find that the encryption method is just an xor of the image
# and the md5 hash of a string.

# We don't know the key used to encrypt the image, but we do know the first 16 bytes of a valid png file.
# Knowing this, we can reverse the xor and get the key, and use the key to decrypt the rest of the image.

# all_encryption_is_equal_but_some_are_more_equal_than_others
