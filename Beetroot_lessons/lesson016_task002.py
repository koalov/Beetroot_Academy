"""Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. Each
Boss has a list of his own workers. You should implement a method that allows you to
add workers to a Boss. You're not allowed to add instances of Boss class to workers
list directly via access to attribute, use getters and setters instead!
You can refactor the existing code.
id_ - is just a random unique integer

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __get__(self):
        return self


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = Boss.__get__(boss)
        self.__get__()

    def __get__(self):
        self.boss.workers.append(self)

    def __str__(self):
        return f'<Worker {self.name} worked in {self.company} company which is ' \
               f'operated by {self.boss.name}>'

    def __repr__(self):
        return f'<Worker {self.name} worked in {self.company} company which is ' \
               f'operated by {self.boss.name}>'


hugo = Boss(1, 'Hugo Johnson', 'Roga ta Kopita')
slave1 = Worker(10, 'Vasyl Pupkin', 'Roga ta Kopita', hugo)
slave2 = Worker(11, 'Valeriy Kurochkin', 'Roga ta Kopita', hugo)
print(hugo.workers)
print(slave1.boss.id)
print(slave2.boss.id)