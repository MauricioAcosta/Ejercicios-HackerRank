(_, A) = (
    raw_input(),
    set(map(int, raw_input().split()))
)

for _ in xrange(input()):
    (command, newSet) = (
        raw_input().split()[0],
        set(map(int, raw_input().split()))
    )

    # Buen truco. Dado que nuestros comandos son nombres de métodos,
    # Ejecute el método en A con nuestro nuevo conjunto como su argumento.
    getattr(A, command)(newSet)

print str(sum(A))

