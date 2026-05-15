class School:
    def __init__(self, school_name, students):
        self.school_name = school_name
        self.__students = students

    def get_students(self):
        return self.__students

    def set_students(self, new_students):
        if new_students <= 10000:
            self.__students = new_students
        else:
            print("Juda ko'p o'quvchi")


s1 = School("45-maktab", 800)

print(s1.school_name)
print(s1.get_students())

s1.set_students(1200)
print(s1.get_students())

s1.set_students(15000)
