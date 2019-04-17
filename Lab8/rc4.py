file = open("secret_key.txt","r")
key = file.read() 
file.close();

def KSA(key):
    keylength = len(key)

    S = range(8)

    j = 0
    for i in range(8):
        j = (j + S[i] + key[i % keylength]) % 8
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 8
        j = (j + S[i]) % 8
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 8]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == '__main__':

    #key = '1236'
    plaintext = '1222'


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