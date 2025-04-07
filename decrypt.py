from manual import des_decrypt_block, pkcs5_unpad

def decrypt_file(infile: str, outfile: str, key: bytes):
    with open(infile, 'rb') as f:
        ciphertext = f.read()
    
    plaintext = bytearray()
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        dec = des_decrypt_block(block, key)
        plaintext.extend(dec)
    
    plaintext = pkcs5_unpad(plaintext)
    with open(outfile, 'wb') as f:
        f.write(plaintext)

if __name__ == '__main__':
    key = b'12345678'
    decrypt_file('file_encrypted.txt', 'file_decrypted.txt', key)
