r=1.2 # infection rate
n=84 # cardinal number
for i in range (1,6):
        n=n*r + n
        # in this circulation, n multiply r constantly then plus previous n so that the ultimate number will be given
print('the r rate is', r ,', the infected students is', n)


