g=open("szemelyek.txt","r",encoding="UTF-8")
személyek=[]
for sor in g:
    sor=sor[:-1]
    listácska=sor.split(";")
    személyek.append(listácska)
g.close()
print(személyek[1][0])
