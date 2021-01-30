# 

O =[100,150,120,125,130]
H =[120,180,200,180,190]
L = [95,55.45,25,76,118.5]
C =[102,85,102.3,108,100]
V =[25000,26000,18000,35000,22000]
T =[15555555,22551515,365454545,54545454,2525252515]

Parameters = [O,H,L,C,V,T]

print (Parameters)

print (sum(V))

average = sum(C)/len(C)

print (average)

print (max(C))




def substract_lists (a,b):
	for i, val in enumerate(a):
		val = val - b[i]


	return a


#price range dificult to find


pricerange = [H[0] - L[0],H[1] - L[1],H[2]-L[2]]

print (pricerange)

V.sort()

print (V.sort(reverse = 0))

print (V)

sortedV = V
print (sortedV)

for i in range(0,100):
	print (i+5+2)

print ("loop ended")































