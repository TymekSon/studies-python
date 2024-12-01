from math import floor

def calculateTime(seconds):
    x = floor(seconds/3600)
    y = floor((seconds-x*3600)/60)
    z = seconds - x*3600 - y*60
    output = (x, y, z)
    return output

def printTime(tuple):
    print("Hours: "+tuple[0])

def main():
    print(calculateTime(3607))

main()
