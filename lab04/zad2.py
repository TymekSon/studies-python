def main():
    A = {1,2,3,4,5}
    B = {2,4,5}

    if(A.intersection(B) == B and A != B):
        print("B jest podzbiorem A")
    elif(B.intersection(A) == A and A != B):
        print("A jest podzbiorem B")
    elif(A == B):
        print("A i B są identyczne")

    inters = A.intersection(B);print("Intersection: ",inters)
    sum = A.union(B);print("Sum: ",sum)
    dif = A.difference(B);print("Difference ",dif)
    symDif = A.symmetric_difference(B);print("Symmetric difference: ",symDif)

main()
