import binascii

def main():
	#print ("Welcome to One Time Pad\n")

	plaintext = "wiki"
	#plaintext = raw_input ("Enter string to encrypt: ")
	#print (binascii.a2b_uu(plaintext))

	binary_of_plain = "01010111 01101001 01101011 01101001"
	#binary_of_plain = ' '.join(format(ord(x), 'b') for x in plaintext)

	binary_of_key = "11110011"
	cypher_binary = ''
	orignal_binary = '' 

	a = binary_of_plain.split(' ')
	for e in a:
		i = 0
		for g in e:
			cypher_binary = cypher_binary + str(int(g)^int(binary_of_key[i]))
			i = i + 1
		cypher_binary = cypher_binary + " "
	print ("Cypher Binary: " + cypher_binary)

	b = cypher_binary.split(' ')

	for e in b:
			i = 0
			for g in e:
				orignal_binary = orignal_binary + str(int(g)^int(binary_of_key[i]))
				i = i + 1
			orignal_binary = orignal_binary + " "
	
	print ("Orignal binary: " + orignal_binary)
main()