import sys
import binascii

def key_to_bytes(key):
    keyinput = list(range(len(key)))
    for c in range(0, len(key)):
        keyinput[c] = ord(key[c])
    return keyinput

def make_stream_source(key):
    keylen = len(key)
    stream = list(range(256))
    j = 0
    for i in range(0, 256):
        j = (j + stream[i] + key[i % keylen]) % 256
        temp = stream[i]
        stream[i] = stream[j]
        stream[j] = temp
    return stream

def gen_stream(key, source):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + source[i]) % 256
        temp = source[i]
        source[i] = source[j]
        source[j] = temp
        k = source[(source[i] + source[j]) % 256]
        print(chr(k))

def main():
    if len(sys.argv) == 2:
        keyinput = sys.argv[1]
    else:
        keyinput = input('enter a key to use: ')
        plaintext = input('enter a string for encrypting: ')
    keyinput = key_to_bytes(keyinput)
    print('key:', keyinput)
    stream_source = make_stream_source(keyinput)
    print('stream source:', stream_source)
    gen_stream(keyinput, stream_source)
    
if __name__ == '__main__':
    main()