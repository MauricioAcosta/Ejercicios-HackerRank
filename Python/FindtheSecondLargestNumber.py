if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    mayor=max(arr)
    while max(arr)==mayor:
        arr.remove(max(arr))
    print(max(arr))
