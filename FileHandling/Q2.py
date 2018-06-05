# Q2.
lst=[]
sum=0
with open("test.txt") as f:
	list=f.readlines()
	for i in list:
		lst.append(i.split())
	for i in range(0,len(lst)):
		sum=sum+len(lst[i])
	print("No. of Words in a file:", sum)
	f.close()


'''
OUTPUT:
No. of Words in a file: 22
'''
