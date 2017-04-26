if __name__ == '__main__':
    num_first=int(input())
    set_first=set(list(map(int, input().split()))[:num_first])
    num_second=int(input())
    set_second=set(list(map(int, input().split()))[:num_second])
    print(len(set_first - set_second))
