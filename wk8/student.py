class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def print(self):
        print(self.name,":", self.id)

    def welcoming(self):
        #print(f"Good morning "+ self.name +", remember your id is "+ str(self.id))
        print("Time to sleep {0}. Log in tomorrow using your id {1} ".format(self.name, self.id))
        