from collections import defaultdict

def main():
    d = defaultdict(lambda : 5)

    for i in range(5):
        key = input("Podaj klucz:")
        print(key + "" + str(d[key]))
        d[key] += 1

main()
