A1 = int(input( "Nota A1: ")) 
A2 = int(input( "Nota A2: "))
P1 = int(input( "Nota P1: "))
P2 = int(input( "Nota P2: "))

#calculando
N1 = (A1 + P1 * 2)/3  #10 6 22/3 7,333 
N2 = (A2 + P2 * 2)/3 #8 6  20/3 6,66

print(N1)
print(N2)

#nota final
NF = (N1 + N2)/2

print("Nota final" , NF)
