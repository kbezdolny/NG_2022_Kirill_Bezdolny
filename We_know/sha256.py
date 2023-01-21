from hashlib import sha256
import itertools

def decodeHash(hash):
    if len(hash) == 64:
        for product in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=4):
            result = ""
            for index in range(len(product)):
                result += product[index]
            if hash == sha256(result.encode()).hexdigest():
                return result
    else:
        return "Hash error!"


print(decodeHash(input("Enter hash: ")))
