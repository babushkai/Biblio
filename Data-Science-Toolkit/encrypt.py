import cryptography.fernet as f
import base64
#base64.b64encode(b'gazQmWzf_emOglxYKH2d2XMHqr0icf4b6rrbbDKz15Q=')

# fernet algorithm is a symmetric, deterministic encryption technique
class ContentObfuscation:
    
    # class atribute for ContentObfuscation
    # Raw key value
    # b'gazQmWzf_emOglxYKH2d2XMHqr0icf4b6rrbbDKz15Q='
    fernetK = b'Z2F6UW1XemZfZW1PZ2x4WUtIMmQyWE1IcXIwaWNmNGI2cnJiYkRLejE1UT0='
    #base64 encoding of the actual key in 
    
    # How do I get the key?
    #import cryptography.fernet as f
    #key = f.Fernet.generate_key()
    #print(key)
    def __init__(self):
        #cipher_suite is an instance of class Fernet, with the encrytion key provided
        #decoded from base64
        self.cipher_suite = f.Fernet(base64.b64decode(ContentObfuscation.fernetK))

    def obfuscate(self, cleartext):
        return self.cipher_suite.encrypt(cleartext)

    def deObfuscate(self, obfuscatedtext):
        return self.cipher_suite.decrypt(obfuscatedtext)
