# Q5.
import random

list = []
f = open('randomnumbers.txt', 'w')

print("There is 10 random numbers and writing them in file: \n")
for i in range(10):
    num = random.randint(1, 100)
    f.write(str(num) + "\n")
f.close()

f1 = open('randomnumbers.txt', 'r+')

list = f1.read().splitlines()
print("Content of the File: \n")
print(list)

for i in range(len(list)):
    list[i] = int(list[i])

list.sort()

f2 = open('sorted.txt', 'w')

for i in range(len(list)):
    f2.write(str(list[i]) + "\n")

f2.close()

f2 = open('sorted.txt', 'r+')
print("Sorted Content: ")
data = f2.read()
print(data)

f.close()
f1.close()
f2.close()

'''
OUTPUT:
There is 10 random numbers and writing them in file: 

Content of the File: 

['87', '9', '86', '7', '35', '82', '88', '70', '52', '6']
Sorted Content: 
6
7
9
35
52
70
82
86
87
88
'''
