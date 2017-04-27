if __name__ == '__main__':
    num_first=int(input())
    set_first=set(list(map(int, input().split()))[:num_first])
    N=int(input())
    for _ in range(N):
        operation=input().split()
        if operation[0]=="intersection_update":
            set_second=set(list(map(int, input().split()))[:len(operation[1])+1])
            set_first.intersection_update(set_second)
            print(set_first)
            print(len(set_first))
        elif operation[0]=="update":
            set_second=set(list(map(int, input().split()))[:len(operation[1])+1])
            set_first.update(set_second)
            print(set_first)
            print(len(set_first))
        elif operation[0]=="symmetric_difference_update":
            set_second=set(list(map(int, input().split()))[:len(operation[1])+1])
            set_first.symmetric_difference_update(set_second)
            print(set_first)
            print(len(set_first))
        elif operation[0]=="difference_update":
            set_second=set(list(map(int, input().split()))[:len(operation[1])+1])
            set_first.difference_update(set_second)
            print(set_first)
            print(len(set_first))
print(len(set_first))
