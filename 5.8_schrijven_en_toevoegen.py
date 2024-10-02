f = open("mijndata.txt", "w")
f.write("dit is regel 1")
f.write(" dit is regel 2")
f.close()

f = open("mijndata.txt", "a")
f.write(" dit is regel 3")
f.write(" dit is regel 4")
f.close()

f = open("mijndata.txt", "r")
inhoud = f.read()
print(inhoud)
f.close()
