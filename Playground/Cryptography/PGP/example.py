"""
Purpose: Demonstrate basic PGP enhancement of crypography

Will use crypto.py's encode and decode, using basic Vigenere cipher for encryption.
Note: it is known that this is not perfect, but will suffice for a simple example.

Reference material:
http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

"""
import string
import random
from crypto import Crypto

class PrettyGoodPrivacy():
    def __init__(self,privateKey):
        self.privateKey = privateKey

    def encodePGP(self,plainMsg):
        # generate random key
        randKey = self._generateRandomKey()
        print("> Internal Random Key: "+randKey)
        # encrypt input with ^
        cryptographer = Crypto()
        encryptedMsg = cryptographer.encode(randKey,plainMsg)
        # encrypt random key with priv. key
        pubKey = cryptographer.encode(self.privateKey,randKey)
        #return concat encrypted key and input
        return pubKey + "_"+encryptedMsg

    def decodePGP(self,concatMsg):
        #parse encrypted pub key, encrypted message
        parsed = concatMsg.split("_")
        pubKey = parsed[0]
        encryptedMsg = parsed[1]
        # decrypt rand key with priv. key
        cryptographer = Crypto()
        randKey = cryptographer.decode(self.privateKey, pubKey)
        # decrypt message with rand key
        decryptedMsg = cryptographer.decode(randKey,encryptedMsg)
        #return message
        return decryptedMsg

    def _generateRandomKey(this,size=8,chars=string.ascii_uppercase+string.ascii_lowercase + string.digits):
        return "".join(random.SystemRandom().choice(chars) for _ in range(size))

def demonstrate():
    print("Note: This example uses an insecure Cipher, but works for the purpose of an example... \n")
    print("Enter a private key: abc123")
    privKey = "abc123"#input()

    print("Enter a message: IamTheOne")
    msg = "IamTheOne"#input()

    pgp = PrettyGoodPrivacy(privKey)
    encMsg = pgp.encodePGP(msg)
    print("Encoded Message: "+encMsg)

    print("\n>>Send your message through unsecure channel here...\n")

    decMsg = pgp.decodePGP(encMsg)
    print("Decoded Message: "+ decMsg)

if __name__ == "__main__":
    demonstrate()
