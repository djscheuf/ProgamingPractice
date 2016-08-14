"""
Purpose: Hosue Vigenere Cipher enc and dec functions for use in example

Reference Material: http://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

"""
import base64

class Crypto:
    def encode(self,key,msg):
        encoded_chars = []
        for i in range(len(msg)):
            key_char = key[i%len(key)]
            encode_char = chr((ord(msg[i])+ord(key_char))%256)
            encoded_chars.append(encode_char)
        return base64.urlsafe_b64encode("".join(encoded_chars))

    def decode(self,key,msg):
        decoded_chars = []
        encoded = base64.urlsafe_b64decode(msg)
        for i in range(len(encoded)):
            key_char = key[i%len(key)]
            decode_char = chr((256 + ord(encoded[i]) - ord(key_char)) % 256)
            decoded_chars.append(decode_char)
        return "".join(decoded_chars)
