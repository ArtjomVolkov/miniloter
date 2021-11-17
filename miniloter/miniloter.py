from random import *
F=randint(1,10)
T=1
S=int(input("Arvake ära täisarv 1 kuni 10 =>"))
while S!=F:
    S=int(input("Palun proovi uuesti =>"))
    if S<F:
        print("Teie number on väiksem, kui arvuti ette nägi")
        T +=1
    elif S>F:
        print("Teie number on suurem, kui arvuti ette nägi")
        T +=1
    else:
        print("Õnnitleme, arvasid ära")
        T +=1
print("Number oli",S)
print("Kui palju katseid oli",T)