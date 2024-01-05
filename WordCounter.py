f = open("WordCounterDemo.txt", "r")
# f is used for open the text file.
# r is used for the read the file.
c = []
# c is the empty list which is later used to store the word from the text file.
for x in f:
    print(x)
    c.append(x.split(' '))
print(c)
# append function to store the data in list.
# split function is used separate the word from file using '' space.
d = 0
# d is for the counter.
for i in range(len(c)):
    d = d + 1
print(d)
print(len(c))