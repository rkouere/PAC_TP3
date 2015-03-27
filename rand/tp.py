import server

# tips http://security.stackexchange.com/questions/17988/how-insecure-are-non-cryptographic-random-number-generators

nextR = 1

def srand(seed):
    global nextR
    nextR = seed

def rand():
    global nextR
    nextR = nextR * 1103515245 + 12345
    return round((nextR/65536) % 32768)


URL="http://pac.bouillaguet.info/TP3"
link_param = "/rand/challenge/echallier"
serverObj = server.Server(URL)

param = serverObj.query(link_param)
print(param)
IV_0 = param["IV"][0]
IV_1 = param["IV"][1]

# on commence le 15 mars 2015 à 00:00:00
#bruteStart = 1426377600

# on fini le jour après le rendu (Thu, 19 Mar 2015 00:00:00 GMT)
# bruteEnd = 1426723200

# IV1 (j'y suis allé à taton... je changeait la valeur en fonction de ce que je recevait !
#IV qui marche

# test
# bruteStart = 590000000
bruteStart  = 0
bruteEnd    = 1426723200


# on cherche a trouver une seed qui marche avec l'IV 1
# while bruteStart < 32768*2:
#     srand(bruteStart)
#     if(rand() == 29395):
#         print(bruteStart)
#     bruteStart += 1

# IV1 = 19350
srand(19350)
print(rand())
srand(9004)
print(rand())

#9004, 29395

#while bruteStart < bruteEnd:
# while True:
#     nextToFind = round((bruteStart/65536) % 32768)
#     print(nextToFind)
#     if nextToFind == IV_0:
#         print("IV0")
#         print(bruteStart)
#         break
#     if nextToFind == IV_1:
#         print("IV1")
#         print(bruteStart)
#         break
#     bruteStart += 1

