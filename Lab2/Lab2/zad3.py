

def main():
    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))
    z = int(input("Podaj z: "))
    c = int(input("Choose an operation 1 +, 2 -, 3 *, 4 / "))

    if c == 1:
        output = x+y+z
    elif c == 2:
        output = x-y-z
    elif c == 3:
        output = x*y*z
    elif c == 4:
        output = x/y/z
    else:
        print("C MUST BE 1 - 4")

    print(output)

main()