class student_list:
    #create a class including First name(Fn), Last name(Ln), Major
    def __init__(self,Fn,Ln,Major):
        self.__Fn = Fn
        self.__Ln = Ln
        self.__Major = Major
    #return corresponding value
    def getFn(self):
        return self.__Fn
    def getLn(self):
        return self.__Ln
    def getMajor(self):
        return self.__Major
#print the example result
student1 = student_list('John','Mark','BMI')
print('The example: His/Her name is ',student1.getFn(),student1.getLn(),', and his/her major is ',student1.getMajor())
#print the input result
student2 = student_list(input('First name is:'),input('Last name is:'),input('The major is:'))
print('His/Her name is ',student2.getFn(),student2.getLn(),', and his/her major is ',student2.getMajor())