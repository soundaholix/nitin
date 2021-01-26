listofnos = []
n =int(input("Enter how many numbers to calculate DMA : "))

for i in range(0, n): 
    nos = int(input())
    listofnos.append(nos)


print (listofnos)
#listofnos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
ma = sum(listofnos)/len(listofnos)
print(ma)#







