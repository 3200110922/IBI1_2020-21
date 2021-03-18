
a=1
b=1
for i in range (1,12):
        c = a + b # define a new variable that equals to a plus b
        a = b # make a equal to b
        b = c # make b equal to c, so that in next circulation new c will be superposed.
        print(c) # c is the result

