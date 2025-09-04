arquivo=open("numeros.txt", "w")
for linha in range(1,50000):
    arquivo.write("%d lais\n" % linha)
arquivo.close()