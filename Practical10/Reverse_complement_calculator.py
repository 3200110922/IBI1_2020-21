#The example sequence
a='aggtctGCTAcATGAag'
print('The example DNA sequence is '+a)
def f(a):
    DNA = {'A':'T','a':'T','T':'A','t':'A','c':'G','C':'G','G':'C','g':'C'}
    #b is equal to the reverse order of a
    b=a[::-1]
    S = ''
    i = 0
    #to get the reverse complement
    while i < len(a):
        S = S + DNA[b[i:i+1]]
        i=i+1
    print('The reverse complement is '+S)
#carry out this function
f(a)
#input a new sequence
a = input('Your DNA sequence is ')
f(a)
