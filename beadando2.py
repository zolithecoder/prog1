#4. feladat



def megoldas(n):
    p = 1
    k = [0]
    s = 1
    while s < 10 ** 9:
        k.append(s)
        s += p + 1
        p += 1
    if n<1 or n>100:
        print("invalid number")
    else:
        for i in range(n):
            a=int(input())
            if a<1 or a>=10**9:
                break
            else:
                for j in range(len(k)):
                    if k[j]>a:
                        print(j-1)
                        break
                    if k[j]==a:
                        print(j)
                        break


try:
    n=int(input())
    if n>=1 and n<=100:
        megoldas(n)
    else:
        print("wrong number")
except ValueError:
    print("The given value could not converted to a number!")
