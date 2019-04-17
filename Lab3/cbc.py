import sys
from operator import methodcaller
import re
import numpy
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random

def main():
    blockSize = 16 # 16-byte encryption
    q1 = cbcDecrypt("140b41b22a29beb4061bda66b6747e14", "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81", blockSize)  
 
def cbcDecrypt(key, cypherText, blockSize):
    print "\nKey/Cypher to be decrypted: ",key," / ",cypherText
    res1 = Decrypt(key, cypherText, blockSize)
    print "Decrypted plaintext: ", res1 
    return res1

def Decrypt(key, cypherText, blockSize):
    k = key.decode('hex')
    ct = cypherText.decode('hex')
    iv = ct[:blockSize]
    ct1 = ct[blockSize:]
    obj = AES.new(k,AES.MODE_CBC,iv)
    paddedStr = obj.decrypt(ct1)
    paddingAmount = ord(paddedStr[len(paddedStr)-1:])
    return paddedStr[:-paddingAmount]

def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

main()
    
