from zad3 import convertToFloat

filepath = "zad4.txt"
file = open(filepath)

array = [[word for word in line.split(",")]for line in file.readlines()]
array = convertToFloat(array)

n = 0
for line in array:
    if line[0] > 5:
        file.write(line)
        n += 1
file.close()


