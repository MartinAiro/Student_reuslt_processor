class Student:
    def __init__(self, name, reg_number, scores):
        self.name = name
        self.reg_number = reg_number
        self.scores = scores

    def calculate_average(self):
        self.average = sum(self.scores) / len(self.scores)
        return self.average

    def classify_result(self):
        if self.average >= 70:
            self.result = "Excellent"
        elif self.average >= 50:
            self.result = "Pass"
        else:
            self.result = "Fail"
        return self.result


students = [
    Student("Ada Lovelace", "REG001", [82, 70, 78]),
    Student("Bo Achieng", "REG002", [60, 54, 48]),
    Student("Cy Otieno", "REG003", [40, 35, 42]),
    Student("Diana Njeri", "REG004", [75, 80, 70]),
    Student("Eliot Kamau", "REG005", [50, 60, 55]),
    Student("Faith Wanjiku", "REG006", [30, 25, 20]),
    Student("George Mwangi", "REG007", [90, 95, 88]),
    Student("Hannah Achieng", "REG008", [65, 70, 60]),
   
]

for s in students:
    s.calculate_average()
    s.classify_result()
    print(s.name, s.reg_number, s.average, s.result)