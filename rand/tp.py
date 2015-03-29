import server

# tips http://security.stackexchange.com/questions/17988/how-insecure-are-non-cryptographic-random-number-generators

nextR = 1

# merci http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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


# test
# on cherche a trouver une seed qui marche avec l'IV_0 et l'IV_1
for i in range(pow(2, 32)):
    if(i%100000000 == 0):
        print("Current i = " + str(i))
    srand(i)
    if(rand() == IV_0):
        if(rand() == IV_1):
            print(bcolors.OKGREEN + str(i) + bcolors.ENDC)

print(bcolors.WARNING + "aucune seed de trouve" + bcolors.ENDC)
        

