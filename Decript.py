import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64
def aes256decrypt(data, AES256key = "DB46CB9B9A1C48A091FA5D66A44D6C77"):
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    private_key = hashlib.sha256(AES256key.encode("utf-8")).digest()
    data = base64.b64decode(data)
    BLOCK_SIZE = AES.block_size
    iv = data[:BLOCK_SIZE]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data[BLOCK_SIZE:])).decode()
print("=====================================================")
input_filename = input("Enter file path that you want to decrpyt : ")
with open(input_filename, "rb") as rp:
    dp = aes256decrypt(rp.read())
    d = dp.encode("utf-8")
    f = base64.b64decode(d)
    outpath = "decrpyt_{}".format(input_filename)
    with open(outpath , "wb") as rp:
        rp.write(f)
