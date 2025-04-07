from manual import des_encrypt_block, pkcs5_pad

def encrypt_file(infile: str, outfile: str, key: bytes):
    with open(infile, 'rb') as f:
        plaintext = f.read()
    plaintext = pkcs5_pad(plaintext)
    
    ciphertext = bytearray()
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        enc = des_encrypt_block(block, key)
        ciphertext.extend(enc)
    
    with open(outfile, 'wb') as f:
        f.write(ciphertext)

if __name__ == '__main__':
    key = b'12345678'  # 密钥
    encrypt_file('file.txt', 'file_encrypted.txt', key)
