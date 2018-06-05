# Q3.
with open("test.txt") as f1, open("test1.txt", "w") as f2:
    data = f1.read()
    f2.write(data)
    f1.close()
    f2.close()
with open("test1.txt") as f3:
    data1 = f3.read()
    print("Content of the 2nd file is:")
    print()
    print(data1)


'''
OUTPUT:
Content of the 2nd file is:

Hello
I am 21 years old
I love playing Cricket
My favourite movie is 3idiots
My favourite TV series is Shelock Holmes

'''