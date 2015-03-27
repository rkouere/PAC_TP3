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
link_param = "/PS3/PK/echallier"
query = "/PS3/sign/echallier"
serverObj = server.Server(URL)


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



param = serverObj.query(link_param)
p = param['p']
g = param['g']
h = param['h']

m0 = 10
m1 = 40

ms0 = serverObj.query(query, {"m": m0})
ms1 = serverObj.query(query, {"m": m1})

s0 = ms0["signature"][1]
s1 = ms1["signature"][1]


r = ms1["signature"][0]
print(type(r))
k = (m0 - m1) * modinv((s0-s1))

x = modinv(r) * (m0-(k*s0))


print(s0)
print(s1)
print(km1)
