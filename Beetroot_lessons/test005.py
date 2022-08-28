class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Student Name: {self.first_name} {self.last_name}'


class Lecturer:
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject

    def __str__(self):
        return f'{self.subject} Lecturer: {self.first_name} {self.last_name}'


class UniversityClass:

    def __init__(self, lecturers=[], students=[]):
        self.lecturers = lecturers
        self.students = students

    def add_student(student):
        raise NotImplementedError

    def remove_student(student):
        raise NotImplementedError

    def add_lecturer(lecturer):
        raise NotImplementedError

    def remove_lecturer(lecturer):
        raise NotImplementedError

    def __iter__(self):
        return UniversityClassIter(self)


class UniversityClassIter:

    def __init__(self, university_class):
        self._lect = university_class.lecturers
        self._stud = university_class.students
        self._class_size = len(self._lect) + len(self._stud)
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self._class_size:
            if self._current_index < len(self._lect):
                member = self._lect[self._current_index]
            else:
                member = self._stud[
                    self._current_index - len(self._lect)]

            self._current_index += 1
            return member

        raise StopIteration


if __name__ == '__main__':
    s1 = Student('Andrew', 'Brown')
    s2 = Student('Helen', 'White')
    s3 = Student('George', 'Johnson')

    l1 = Lecturer('Maria', 'Richardson', 'Algorithms')
    l2 = Lecturer('Bob', 'Johanson', 'Programming')

    uni_cl = UniversityClass(lecturers=[l1, l2], students=[s1, s2, s3])

    for i in range(len(uni_cl)):
        if i % 2 == 0:
            continue
        print(uni_cl[i])