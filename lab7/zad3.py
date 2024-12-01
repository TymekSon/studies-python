filepath = "iris.txt"

def convertToFloat(array):
    newArray = []
    for line in array:
        subArray = []
        for word in line:
            try:
                subArray.append(float(word))
                print("Converted to float")
            except: 
                subArray.append(word)
                print("Cannot convert to float")  
        newArray.append(subArray)
    return newArray
                
file = open(filepath)
lines = file.readlines()
array = [[word for word in line.split(",")]for line in lines]

print(array[1][3])

convertToFloat(array)

file.close()
