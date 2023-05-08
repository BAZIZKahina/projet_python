
class professor:

    #class variable
    university_name = "Golden"

    def __init__(self, name, age, department, course, classe, table, computer, salary, skill, job ):
       
        # Attribus d'instance
        self.name = name
        self.age = age
        self.department = department
        self.course = course
        self.classe = classe
        self.table = table
        self.computer = computer
        self.salary = salary
        self.skill = skill
        self.job = job


        # méthodes
        def get_name (self):
            return self.name
        
        def set_name (self, name):
            self.name = name

        def get_age (self):
            return self.age

        def set_age (self,age):
            self.age = age
        
        def get_department (self):
            return self.department

        def set_department (self, department):
            self.department = department
        
        def get_course (self):
            return self.course

        def set_course (self,course):
            self.course = course

        def get_classe (self):
            return self.classe

        def set_classe (self, classe):
            self.classe = classe

        def get_table (self):
            return self.table

        def set_table (self, table):
            self.table = table
        
        def get_computer (self):
            return self.comptuer

        def set_computer (self, computer):
            self.computer = computer
        
        def get_salary (self):
            return self.salary

        def set_salary (self, salary):
            self.salary = salary
         
        def get_skill (self):
            return self.skill

        def set_skill (self, skill):
            self.skill = skill
        
        def get_job (self):
            return self.job

        def set_job (self, job):
            self.job = job

        # salary
        if salary < 1200:
            self.is_salary = True
        else:
            self.is_salary = False

        # classe
        if classe <= 26:
            self.is_classe = True
        else:
            self.is_classe = False

        # course
        if course >= 10:
            self.is_course = True
        else:
            self.is_course = False

        # job
        for job in self.job:
            return self.job
        i = 1
        while i < len(self.job):
            i = 1
            return self.job
            