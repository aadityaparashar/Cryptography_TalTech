from Crypto.Cipher import DES3
from Crypto import Random

key = 'Sixteen byte key'
IV = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, IV)
plaintext = 'Implement threeDES in any programming language          '
encrypted_text = cipher_encrypt.encrypt(plaintext)

cipher_decrypt = DES3.new(key, DES3.MODE_OFB, IV)
print(encrypted_text)
print(cipher_decrypt.decrypt(encrypted_text))