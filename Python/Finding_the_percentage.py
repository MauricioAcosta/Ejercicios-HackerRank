if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    promedio=student_marks.get(query_name)
    suma=0
    for i in promedio:
        suma=i+suma
    print("{0:.2f}".format(suma/3))
