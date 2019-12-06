

def header_footer(n):
    for i in range(0, n*2):
        print("-", end='')
    print('')


def shapes(n):
    print("-", end='')
    for i in range(0, n-1):
        print("\\/", end='')
    print("-")


numberActual = int(input())

def result(number):
    header_footer(number)
    for i in range(0, number-2):
        shapes(number)
    header_footer(number)

result(numberActual)