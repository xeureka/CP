class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber) 
        self.scores = scores

    def calculate(self):
        summ = sum(self.scores) 

        gradeNumber = summ / len(self.scores)

        if 90 <= gradeNumber <= 100:
            return 'O'
        elif 80 <= gradeNumber < 90:
            return 'E'
        elif 70 <= gradeNumber < 80:
            return 'A'
        elif 55 <= gradeNumber <70:
            return 'P'
        elif 40 <= gradeNumber < 55:
            return 'D'
        else:
            return 'T'

        
