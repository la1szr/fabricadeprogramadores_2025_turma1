L=[]
while True:
    n=(input("digite uma palavra:"))
    if n == "p":
            break
    L.append(n)
x=0
while x < len(L):
    print(L[x])
    x=x+1
    
print(L)