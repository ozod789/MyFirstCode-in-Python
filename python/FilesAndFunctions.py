""" f = open('data.txt', "rb")
data = f.read()
print(data)
f.close()

f = open('data1.txt', 'a')
data1 = f.write("Hello there, how are you, is everything okey!!!")
f.close()

 """

def storeFile(file):
    f = open(file, 'r')
    contents = f.read()
    f.close()
    return contents

varText = 'data.txt'
print(storeFile(varText))