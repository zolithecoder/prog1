#1. feladat


def game(korok):
    p1 = 0
    p2 = 0
    #vezet = ""
    #mennyivel = 0
    l = []
    m = 0
    p = ""
    for i in range(korok):
        k=input()
        l=k.split()
        p1+=int(l[0])
        p2+=int(l[1])
        if p1>p2:
            #vezet="p1"
            mennyivel=p1-p2
            #print(vezet)
            #print(mennyivel)
            if mennyivel>m:
                m=mennyivel
                p="P1"
        else:
            #vezet="p2"
            mennyivel=p2-p1
            #print(vezet)
            #print(mennyivel)
            if mennyivel > m:
                m = mennyivel
                p="P2"

    print('{} {}'.format(p,m))


korok=int(input())
game(korok)




