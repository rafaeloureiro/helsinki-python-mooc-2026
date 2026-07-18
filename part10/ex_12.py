"""
An interactive application for keeping track of studies.
Each course name should result in a single entry in the records. 
A grade may be raised by re-entering the course details, but the grade should never be lowered.
"""

class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def update(self, grade: int, credits: int):
        self.__credits = credits
        if grade > self.__grade:
            self.__grade = grade

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"


class StudyRegister:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name].update(grade, credits)

    def get_course(self, name: str):
        if name not in self.__courses:
            return None
        return self.__courses[name]

    def all_courses(self):
        return self.__courses


class StudyRegisterApplication:
    def __init__(self):
        self.__register = StudyRegister()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__register.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        course = self.__register.get_course(name)
        if course is None:
            print("no entry for this course")
            return
        print(course)

    def statistics(self):
        courses = self.__register.all_courses()
        number_of_courses = len(courses)
        total_credits = 0
        total_grades = 0
        distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        for course in courses.values():
            total_credits += course.credits()
            total_grades += course.grade()
            distribution[course.grade()] += 1

        print(f"{number_of_courses} completed courses, a total of {total_credits} credits")

        if number_of_courses > 0:
            mean = total_grades / number_of_courses
            print(f"mean {mean:.1f}")

        print("grade distribution")
        for grade in range(5, 0, -1):
            print(f"{grade}: {'x' * distribution[grade]}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()


application = StudyRegisterApplication()
application.execute()
