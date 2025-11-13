class Person:
    def __init__(self, first_name, surname, age, postcode):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.postcode = postcode
    def getgreeting(self): #is get needed, can I just run method without get, it's output shld be same
        print('Hello, my name is %s, %s. I am %d years old and my postcode is %s' % (self.first_name, self.surname, self.age, self.postcode)) #
        
class Student(Person):
    def __init__(self, first_name, surname, age, postcode, student_ID, degree_subject):
        super().__init__(first_name, surname, age, postcode) # I think this expands the sub-class with super-class features
        self.student_ID = student_ID
        self.degree_subject = degree_subject
    def getstudentGreeting(self): 
        super().getgreeting()
        print('My student ID is %s and I am reading %s' % (self.student_ID, self.degree_subject))
        

if __name__ == '__main__':
        
	student1=Student('Dick', 'Turpin', 32, 'HP11 2JZ', 'DT123456', 'Highway Robbery')
	student2=Student('Dorothy', 'Turpin', 32, 'SO14 7AA', 'DT123457', 'Law')
	student3=Student('Oliver', 'Cromwell', 32, 'OX35 14RE', 'OC123456', 'History')
	students = [student1, student2, student3]

	for i in students:
		i.getstudentGreeting()
