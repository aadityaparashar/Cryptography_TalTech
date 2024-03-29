file = open("secret_key.txt","r")
key = file.read() 
file.close();

def KSA(key):
    keylength = len(key)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == '__main__':

    # ciphertext should be BBF316E8D940AF0AD3 for 256 bit
    #key = '1236'
    plaintext = '1222'

    # ciphertext should be 1021BF0420 for 256 bit
    #key = 'Wiki'
    #plaintext = 'pedia'

    # ciphertext should be 45A01F645FC35B383552544B9BF5 for 256 bit
    #key = 'Secret'
    #plaintext = 'Attack at dawn'

    def convert_key(s):
        return [ord(c) for c in s]
    key = convert_key(key)

    keystream = RC4(key)

    import sys
    print ""
    print "Message Encrypted using RC4 with key extablished using D-H logic"
    for c in plaintext:
        sys.stdout.write("%02X" % (ord(c) ^ keystream.next()))
    print