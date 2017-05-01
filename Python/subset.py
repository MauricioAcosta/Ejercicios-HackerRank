for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    var = True if (A<=B) else False
    print (var)
