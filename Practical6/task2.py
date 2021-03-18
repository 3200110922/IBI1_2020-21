import matplotlib.pyplot as plt

biaoqian = 'USA','India','Brazil','Russia','UK' # set up a labels called 'biaoqian'
bili = [29862124,11285561,11205972,4360823,4234924] # set up a list called 'bili'
explode = (0.1,0.1,0.1,0.1,0.1) # make every part's interspace 0.1
plt.pie(bili, explode=explode, labels=biaoqian,autopct='%1.1f%%', shadow= False, startangle=90) # set up a new pie graph 
plt.axis('equal') # Make the scales equal in length
plt.show()

