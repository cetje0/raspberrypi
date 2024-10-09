f = open("mijndata.txt", "w")
f.write("dit is regel 1\n")
f.write("dit is regel 2\n")
f.close()

f = open("mijndata.txt", "a")
f.write("dit is regel 3\n")
f.write("dit is regel 4")
f.close()

f = open("mijndata.txt", "r")
inhoud = f.read()
print(inhoud)
f.close()
