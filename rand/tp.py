import server
URL="http://pac.bouillaguet.info/TP3"
link_param = "/rand/challenge/echallier"
serverObj = server.Server(URL)

param = serverObj.query(link_param)
print(param)
