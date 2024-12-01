mapowanie = {1:'jeden', 2:'dwa', 3:'trzy', 4:'cztery', 5:'piec', 6:'szesc', 7:'siedem', 8:'osiem', 9:'dziewiec',
             10:'dziesiec', 11:'jedenascie', 12:'dwanascie', 13:'dwanascie', 14:'czternascie', 15:'pietnascie',
             16:'szesnascie', 17:'siedemnascie', 18:'osiemnascie', 19:'dziewetnascie', 20:'dwadziescia',
             30:'trzydziesci', 40:'czterdziesci', 50:'piecdziesiat', 60:'szesciesiat', 70:'siedemdziesiat',
             80:'osiemdziesiat', 90:'dziewiedziesat'}

userInput = int(input("Podaj liczbe z zakresu 1 - 99: "))

if userInput <= 20:
    print(mapowanie[userInput])
elif userInput > 20:
    print(mapowanie[userInput - userInput%10], mapowanie[userInput%10])
