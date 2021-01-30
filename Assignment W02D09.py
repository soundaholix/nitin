ohlc1 = [126,138,140,102,20400,4545454545]
ohlc2 = [125,130,145,102,20555,5515151515]
ohlc3 = [125,135,145,102,20044,4545488787]
ohlc4 = [125,139,145,106,23222,5656565656]
ohlc5 = [125,134,145,102,22233,8788787878]



for i in range(0,(len(ohlc1))):
	print (ohlc1[i])
	i+1

weekly = [ohlc1,ohlc2,ohlc3,ohlc4,ohlc5]
print (weekly)

sumlist=[]
s=0
for j in weekly:
	for k in weekly[s]:
		print(weekly[s][4])
		sumlist.append(weekly[s][4])
		break

	s=s+1

print (sum(sumlist))














		

		
	


		
	
	

	

	
	










































