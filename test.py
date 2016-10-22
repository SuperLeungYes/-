filename1 = raw_input("enter file 1:")
filename2 = raw_input("enter file 2:")
f1 = open(filename1,'r')
f2 = open(filename2,'r')
line1 = f1.readlines()
line2 = f2.readlines()
len1 = len(line1)
len2 = len(line2)
heng = len1 if len1 <= len2 else len2
for i in range(heng):
	if cmp(line1[i],line2[i]) != 0:
		print "row is %d." %(i+1)
		len3 = len(line1[i])
		len4 = len(line2[i])
		shu = len3 if len3 <= len4 else len4
		for j in range(shu):
			if cmp(line1[i][j],line2[i][j]) != 0:
				print "zhonglie is %d." %(j+1)
				break
		break
else:
	if len1 == len2:
		print "the file is equal."
	else:
		print "row is %d." %(i+1)