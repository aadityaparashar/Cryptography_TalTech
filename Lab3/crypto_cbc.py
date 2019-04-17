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
    q2 = cbcDecrypt("140b41b22a29beb4061bda66b6747e14", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253", blockSize)  
    
    print "\n\nAnswers:"
    print "Q1. ",q1
    print "Q2. ",q2

def cbcDecrypt(key, cypherText, blockSize):
    print "\nCBC decryption of key/cypher",key," / ",cypherText
    res1 = cbcDecrypt1(key, cypherText, blockSize)
    res2 = cbcDecrypt2(key, cypherText, blockSize)
    print "1: ", res1 
    print "2: ", res2
    return res2

# CBC decryption variant 1 (use AES.MODE_CBC mode), 
def cbcDecrypt1(key, cypherText, blockSize):
    k = key.decode('hex')
    ct = cypherText.decode('hex')
    iv = ct[:blockSize]
    ct1 = ct[blockSize:]
    obj = AES.new(k,AES.MODE_CBC,iv)
    paddedStr = obj.decrypt(ct1)
    paddingAmount = ord(paddedStr[len(paddedStr)-1:])
    return paddedStr[:-paddingAmount]


# CBC decryption variant 2 defines blocks self, encrypts per block (ECB mode) and xors with previous block => plaintext
def cbcDecrypt2(key, cypherText, blockSize):
    cypherTextBlocks =  [cypherText[i:i+(blockSize*2)] for i in range(0, len(cypherText), (blockSize*2))]
    cypherTextBlocksDecoded = map(methodcaller("decode", "hex"), cypherTextBlocks)
    #iv =  cypherTextBlocksDecoded.pop(0)
    k = key.decode('hex')

    pt = ""

    iter = len(cypherTextBlocksDecoded)
    for c in reversed(cypherTextBlocksDecoded):
        iter = iter - 1
        if(iter > 0):
            cipher = AES.new(k, AES.MODE_ECB).decrypt(c)            
            plaintext = strxor(cipher, cypherTextBlocksDecoded[iter - 1])
            #print "[",iter,"]", c.encode('hex'), " => ", cipher.encode('hex'), plaintext
            pt = plaintext + pt

    paddingAmount = ord(pt[len(pt)-1:])
            
    return pt[:-paddingAmount]


# xor two strings of different lengths
def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

main()
    

