# Q4.
i=0
j=0
with open("test.txt") as f1,open("sample.txt") as f2:
	lst1=f1.read().splitlines()
	lst2=f2.read().splitlines()
	if(len(lst1)==len(lst2)):
		for i in range(len(lst1)):
			print(lst1[i]+" "+lst2[i])
	elif(len(lst1)<len(lst2)):
		for i in range(len(lst1)):
			print(lst1[i]+" "+lst2[i])
		for j in range(len(lst1),len(lst2)):
			print(lst2[j])
	else:
		for i in range(len(lst2)):
			print(lst1[i]+" "+lst2[i])
		for j in range(len(lst2),len(lst1)):
			print(lst1[j])
	f2.close()
	f1.close()


'''
OUTPUT:
Hello Hello
I am 21 years old This is 2nd line
I love playing Cricket This is 3rd line
My favourite movie is 3idiots This is 4th line
My favourite TV series is Shelock Holmes This is 5th line
'''