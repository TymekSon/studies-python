filepath = "iris.txt"

file = open(filepath)
lines = file.readlines()
array = [[word for word in line.split(",")]for line in lines]

print(array)

file.close()
