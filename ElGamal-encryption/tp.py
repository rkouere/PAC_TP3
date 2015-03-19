import server
import math


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
 




URL="http://pac.bouillaguet.info/TP3"
link_param = "/ElGamal-encryption/parameters/echallier"
serverObj = server.Server(URL)


param = serverObj.query(link_param)
p = param['p']
g = param['g']

x = 100

PK = pow(g, x, p)
reply = serverObj.query("/ElGamal-encryption/challenge/echallier", {'h': PK})
text_to_decrypt = reply['ciphertext']
a = text_to_decrypt[0]
b = text_to_decrypt[1]

h = modinv(pow(a, x, p), p)
#print(mes1)

# faire une division en modulo = multiplier par l'inverse mod p
plaintext = b*h%p
print(plaintext)
print(serverObj.query("/ElGamal-encryption/validate/echallier", {'plaintext': plaintext}))
