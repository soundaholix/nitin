#pivot strategy

Popen = 14500
Phigh = 14600
Plow = 14400
Pclose = 14650

Cpivot = (Phigh + Plow + Pclose)/3
R1 = Cpivot*2 - Plow
S1 = Cpivot*2 -Phigh
S2 = Cpivot - (Phigh - Plow)
R2 = Cpivot + (R1 - S1)
R3 = Cpivot - (R2- S2)
S3 = S1 - (Phigh - Plow)

print ("R1 is ",R1)
print ("R2 is ",R2)
print ("S1 is ",S1)
print ("S2 is ",S2)
print ("R3 is ",R3)
print ("S3 is ",S3)
print ("Copivot is ",Cpivot)





