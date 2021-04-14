class grade_calculator:
    def __init__(self,sn,cg,pg,fg):
        self.__sn = sn
        self.__cg = cg
        self.__pg = pg
        self.__fg = fg
    #calculate the total grade
    def getgrade(self):
        grade = self.__cg * 0.4 + self.__fg * 0.3 + self.__pg * 0.3
        return round(grade * 100)/100

    def getname(self):
        return self.__sn
#print the example result
student1 = grade_calculator('John',88,76,90)
print(student1.getname(),'total grade is ',student1.getgrade())
#input your information
a=input('Your name is:')
b=input('your code portfolio grade is:')
c=input('your poster presentation grade is:')
d=input('your final exam grade is:')
student2 = grade_calculator(a,int(b),int(c),int(d))
print(student2.getname(),', your total grade is ',student2.getgrade())