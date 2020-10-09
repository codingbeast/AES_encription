import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64
def aes256encrypt(data, AES256key = "DB46CB9B9A1C48A091FA5D66A44D6C77"):
    BLOCK_SIZE = AES.block_size
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    private_key = hashlib.sha256(AES256key.encode("utf-8")).digest()
    raw = pad(data)
    raw = raw.encode("utf8")
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw)).decode()
print("=====================================================")
input_filename = input("Enter file path : ")
with open(input_filename, "rb") as rp:
    b64string = base64.b64encode(rp.read())
    a= aes256encrypt(b64string.decode("utf-8"))
    outpath = "Encript_{}".format(input_filename)
    with open(outpath, "w") as rp:
        rp.write(a)