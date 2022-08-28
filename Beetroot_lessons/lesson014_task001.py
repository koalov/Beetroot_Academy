"""School

Make a class structure in python representing people at school. Make a base class
called Person, a class called Student, and another one called Teacher. Try to find
as many methods and attributes as you can, which belong to different classes, and
keep in mind which are common and which are not. For example, the name should be
a Person attribute, while salary should only be available to the teacher. """


class Person:
    def __init__(self, name, surname, age, email, country, address, gender,
                 marital_status):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.country = country
        self.address = address
        self.gender = gender
        self.marital_status = marital_status

    def get_info(self):
        print(self.name + " " + self.surname + " ==> class " + self.__class__.__name__)
        print("\n", "=" * 50, "\n")
        for key, value in self.__dict__.items():
            print(f"{key} ==> {value}")
        print("\n", "=" * 50, "\n")


class Student(Person):
    def __init__(self, name, surname, age, country, address, email, gender,
                 marital_status, institution, specialization, year_of_study,
                 mean_grade, scholarship):
        super().__init__(name, surname, age, country, address, email, gender,
                         marital_status)
        self.institution = institution
        self.specialization = specialization
        self.year_of_study = year_of_study
        self.mean_grade = mean_grade
        self.scholarship = scholarship


class Teacher(Person):
    def __init__(self, name, surname, age, country, address, email, gender,
                 marital_status, education, degree, experience, salary, profession):
        super().__init__(name, surname, age, country, address, email, gender,
                         marital_status)
        self.education = education
        self.degree = degree
        self.experience = experience
        self.salary = salary
        self.profession = profession


vasya = Person("Vasya", "Pupkin", 45, "vasya.pupkin@example.com", "Ukraine",
               "Kyiv, I. Franka str. 15", "male", "married")

vera = Student("Vera", "Pupkina", 19, "Ukraine", "Kyiv, I. Franka str. 15",
               "vera.pupkina@example.com", "female", "single",
               "Kyievo-Mogylans'ka Academy", "Software Developer", 4, 89, 6300)

ira = Teacher("Irina", "Pupkina", 43, "Ukraine", "Kyiv, I. Franka str. 15",
              "irina.pupkina@example.com", "female", "married", "High", "Dr.", 17,
              18500, "Professor")

vasya.get_info()
vera.get_info()
ira.get_info()
