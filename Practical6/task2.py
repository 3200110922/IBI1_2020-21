import matplotlib.pyplot as plt

biaoqian = 'USA','India','Brazil','Russia','UK'
bili = [29862124,11285561,11205972,4360823,4234924]
explode = (0.1,0.1,0.1,0.1,0.1)
plt.pie(bili, explode=explode, labels=biaoqian,autopct='%1.1f%%', shadow= False, startangle=90)
plt.axis('equal')
plt.title('example:Comparing coronavirus infection rates across countries')
plt.show()
for i in range(1,6):
    change=[]
    n = int(input())
    change.append(n)
plt.pie(bili, explode=explode, labels=biaoqian,autopct='%1.1f%%', shadow= False, startangle=90)
plt.axis('equal')
plt.title('change:Comparing coronavirus infection rates across countries')
plt.show()