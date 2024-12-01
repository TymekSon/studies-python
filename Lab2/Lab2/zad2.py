import math

def calculate(x, y):
    output = math.e + math.log10(math.pow(x,2)+1)*((x-1)/math.cos(math.pow(y,3)-1)+6)
    return output

def main():
    try:
        x = float(input("Podaj wartość x: "))
        y = float(input("Podaj wartość y: "))
        print(calculate(x, y))
    except:
        print("must be float not str")
main()