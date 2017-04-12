if __name__ == '__main__':
    datos=[]
    for _ in range(0,int(input())):
        datos.append([input(), float(input())])
    segundo_grado = sorted(list(set([dato for nombre,dato in datos])))[1]
    print('\n'.join([a for a,b in sorted(datos) if b==segundo_grado]))
