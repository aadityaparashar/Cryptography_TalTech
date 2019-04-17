import hashlib
import time
from random import choice
import string
import sys

if (len(sys.argv) > 1):
	for x in xrange(1,len(sys.argv)):
		if(sys.argv[x] == "pt"):
			plaintext = sys.argv[x+1]
else:
	plaintext = "Some random string"

def salt(length, chars=string.ascii_letters):
    return ''.join([choice(chars) for i in range(length)])

salt = salt(10)

def md5():
	md5_start = time.time()

	m = hashlib.md5()
	m.update(plaintext+salt)
	print "MD5: "+m.hexdigest()

	md5_end = time.time()
	md5_time = md5_end - md5_start

	return md5_time

def sha1():
	sha1_start = time.time()

	sha1_hashed = hashlib.sha1(plaintext+salt)
	print "SHA1: " + str(sha1_hashed.hexdigest())

	sha1_stop = time.time()
	sha1_time = sha1_stop - sha1_start
	return sha1_time

def sha256():
	sha256_start = time.time()

	sha256_hashed = hashlib.sha256(plaintext+salt)
	print "SHA256: " + str(sha256_hashed.hexdigest())

	sha256_stop = time.time()
	sha256_time = sha256_stop - sha256_start

	return sha256_time


if __name__ == '__main__':

	print ""
	md5_time = md5()
	sha1_time = sha1()
	sha256_time = sha256()

	print ""
	print "Plaintext: " + plaintext + " <--> Salt: " + salt

	print "Time taken for MD5 hash of plaintext is: " + str(md5_time) + "s"
	print "Time taken for SHA1 hash of plaintext is: " + str(sha1_time) + "s"
	print "Time taken for SHA-256 hash of plaintext is: " + str(sha256_time) + "s"
