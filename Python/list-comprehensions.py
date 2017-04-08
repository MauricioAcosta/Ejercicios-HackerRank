if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    combinaciones=[(i,j,k)for i in [X,Y-1,Z-1]for j in [X-1,Y,Z-1]for k in [X-1,Y-1,Z] if 0<= i <= X if 0<= j<=Y if 0<=k<=Z if (i+j+k)!=N]
    combinaciones.append((0,0,0))
    print(combinaciones)
    combinacionSinRepetir=[]
    for i in combinaciones:
        if list(i) not in combinacionSinRepetir:
            combinacionSinRepetir.append(list(i))
            combinacionSinRepetir.sort()
    print(combinacionSinRepetir)
