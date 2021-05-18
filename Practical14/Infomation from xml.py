import xml.dom.minidom
from xml.dom.minidom import parse
DOM= xml.dom.minidom.parse("go_obo.xml")
collection = DOM.documentElement
terms= collection.getElementsByTagName('term')        #Read the file and make a DOM tree
def countnum(a):                #Define a function that count the childnode number of 'a'-assosiated terms
    count=0
    for term in terms:                     #Get the element 'term'
        defstr=term.getElementsByTagName('defstr')      #From term get element 'defstr'          
        if a in defstr[0].firstChild.data:                     
            subclass=term.getElementsByTagName('is_a')           # If 'a' exists in 'defstr', then read the 'is_a' of it
            for is_a in subclass:
                count= count+ 1                  #Add the counts
    print('The childnode number of '+a+' is '+ str(count)+'.')
    return count
DNA=countnum('DNA')
RNA=countnum('RNA')
Protein=countnum('protein')
GP=countnum('glycoprotein')                   # I am interested in the number of childNotes related with glycoprotein
import matplotlib.pyplot as plt
dic={'DNA':DNA,'RNA':RNA,'Protein':Protein,'glycoprotein':GP}
sum= dic['DNA']+dic['RNA']+dic['Protein']+dic['glycoprotein']       # the sum of all cases
labels='DNA','RNA','Protein','glycoprotein'
sizes=[100*dic['DNA']/sum,100*dic['RNA']/sum,100*dic['Protein']/sum,100*dic['glycoprotein']/sum]    # the percentage of cases is count by "100*X/sum"
explode=(0,0.1,0,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('The childNodes number of different molequle-assosiated terms.')
plt.show()        # make the plot and draw