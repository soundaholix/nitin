ohlc1 = [126,138,140,102,20400,4545454545]
ohlc2 = [125,130,145,102,20555,5515151515]
ohlc3 = [125,135,145,102,20044,4545488787]
ohlc4 = [125,139,145,106,23222,5656565656]
ohlc5 = [125,134,145,102,22233,8788787878]


pricelist =[ohlc1,ohlc2,ohlc3,ohlc4,ohlc5]

i = 0
while i < len(pricelist):
		print (pricelist[i])
		i=i+1



#make an empty list, add the vol for each list to the new list and then summation. 
indexlist = []

i = 0
while i < len(pricelist):
	  indexlist.append(pricelist[i][4])
	  print (pricelist[i][4])

	  i = i + 1

print (indexlist)

avgvol = sum(indexlist)/len(pricelist)
print (avgvol)

# find highest closing price in 5 lists, need to find out closing in every list and find max among these..empty set, add closing and find max


# price_range, high - low for each day and add them to a new list called highlowdiff

highlowdiff = []
i = 0
while i < len(pricelist):
	highlowdiff.append(pricelist[i][2]-pricelist[i][1])
	i = i + 1

print (highlowdiff)









































